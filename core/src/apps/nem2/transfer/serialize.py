from trezor.crypto import random, base32
from trezor.messages.NEMTransactionCommon import NEMTransactionCommon
from trezor.messages.NEMTransfer import NEMTransfer
from ubinascii import hexlify, unhexlify

from ..helpers import (
    AES_BLOCK_SIZE,
    NEM2_TRANSACTION_TYPE_TRANSFER,
)

from ..writers import (
    serialize_tx_common,
    get_common_message_size,
    serialize_embedded_tx_common,
    get_embedded_common_message_size
)

from apps.common.writers import (
    write_bytes,
    write_uint8,
    write_uint16_le,
    write_uint32_le,
    write_uint64_le
)
# reflect the serialization used here:
# https://github.com/nemtech/nem2-sdk-typescript-javascript/blob/master/src/infrastructure/catbuffer/TransferTransactionBodyBuilder.ts#L120
def serialize_transfer(
    common: NEM2TransactionCommon | NEM2EmbeddedTransactionCommon,
    transfer: NEM2TransferTransaction,
    embedded = False
) -> bytearray:
    tx = bytearray()

    # Total size is the size of the common transaction properties
    # + the transfer transaction specific properties
    size = get_common_message_size() if not embedded else get_embedded_common_message_size()
    size += get_transfer_body_size(transfer)

    # Write size
    write_uint32_le(tx, size)
    # Write the common properties
    serialize_tx_common(tx, common) if not embedded else serialize_embedded_tx_common(tx, common)
    # Write the transfer transaction body
    write_bytes(tx, serialize_transfer_body(transfer))

    return tx

def serialize_transfer_body(
    transfer: NEM2TransferTransaction
) -> bytearray:
    tx = bytearray()

    # recipient_address (catbuffer UnresolvedAddress - 25 bits) base 32 encoded
    write_bytes(tx, base32.decode(transfer.recipient_address.address))

    # mosaics count (1 byte)
    write_uint8(tx, len(transfer.mosaics))

    # message size (1 byte for type + n bytes for message payload size)
    write_uint16_le(tx, 1 + len(transfer.message.payload.encode()))

    # transfer tx reserved bytes (4 bytes)
    write_uint32_le(tx, 0)

    # mosaics
    for mosaic in transfer.mosaics:
        serialize_mosaic(tx, mosaic.id, mosaic.amount)

    # message type (1 bytes)
    write_uint8(tx, transfer.message.type)

    #message payload (<message size> bytes)
    write_bytes(tx, transfer.message.payload.encode())

    return tx

def get_transfer_body_size(transfer):
    # Add up the transfer-specific message attribute sizes
    size = 25 # recipient_address (catbuffer UnresolvedAddress)
    size += 2 # message size
    size += 1 # mosaics count
    size += 1 + len(transfer.message.payload.encode()) # message type takes up 1 byte
    size += len(transfer.mosaics) * (8 + 8) # 8 bytes id + 8 bytes amount (catbuffer Mosaic)
    size += 4 # reserved bytes
    return size

def serialize_mosaic(w: bytearray, mosaic_id: str, amount: int):
    write_uint64_le(w, int(mosaic_id, 16))
    write_uint64_le(w, int(amount))

def serialize_importance_transfer(
    common: NEMTransactionCommon, imp: NEMImportanceTransfer, public_key: bytes
) -> bytearray:
    w = serialize_tx_common(
        common, public_key, NEM_TRANSACTION_TYPE_IMPORTANCE_TRANSFER
    )

    write_uint32_le(w, imp.mode)
    write_bytes_with_len(w, imp.public_key)
    return w


def get_transfer_payload(transfer: NEM2Transfer, node) -> [bytes, bool]:
    payload = transfer.payload
    encrypted = False
    if transfer.public_key is not None:
        if payload is None:
            raise ValueError("Public key provided but no payload to encrypt")
        payload = _encrypt(node, transfer.public_key, transfer.payload)
        encrypted = True

    return payload, encrypted


def _encrypt(node, public_key: bytes, payload: bytes) -> bytes:
    salt = random.bytes(NEM_SALT_SIZE)
    iv = random.bytes(AES_BLOCK_SIZE)
    encrypted = node.nem_encrypt(public_key, iv, salt, payload)
    return iv + salt + encrypted


def _get_version(network, mosaics=None) -> int:
    if mosaics:
        return network << 24 | 2
    return network << 24 | 1


def canonicalize_mosaics(mosaics: list):
    if len(mosaics) <= 1:
        return mosaics
    mosaics = merge_mosaics(mosaics)
    return sort_mosaics(mosaics)


def are_mosaics_equal(a: NEM2Mosaic, b: NEM2Mosaic) -> bool:
    if a.id == b.id:
        return True
    return False


def merge_mosaics(mosaics: list) -> list:
    if not mosaics:
        return []
    ret = []
    for i in mosaics:
        found = False
        for k, y in enumerate(ret):
            if are_mosaics_equal(i, y):
                ret[k].amount += i.amount
                found = True
        if not found:
            ret.append(i)
    return ret


def sort_mosaics(mosaics: list) -> list:
    return sorted(mosaics, key=lambda m: (m.namespace, m.mosaic))