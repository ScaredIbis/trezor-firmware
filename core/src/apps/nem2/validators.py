from trezor.messages.NEM2SignTx import (
    NEM2SignTx,
    NEM2TransactionCommon,
    NEM2TransferTransaction,
    NEM2HashLockTransaction
)
from trezor.wire import ProcessError

from .helpers import (
    NEM2_MAX_DIVISIBILITY,
    NEM2_MAX_ENCRYPTED_PAYLOAD_SIZE,
    NEM2_MAX_PLAIN_PAYLOAD_SIZE,
    NEM2_MAX_SUPPLY,
    NEM2_NETWORK_MAIN_NET,
    NEM2_NETWORK_MIJIN,
    NEM2_NETWORK_TEST_NET,
    NEM2_PUBLIC_KEY_SIZE,
)

from .namespace.validators import (
    _validate_namespace_registration,
    _validate_address_alias
)

def validate(msg: NEM2SignTx):
    if msg.transaction is None:
        raise ProcessError("No common transaction fields provided")

    _validate_single_tx(msg)
    _validate_common(msg.transaction)

    if msg.multisig:
        _validate_common(msg.multisig, True)
        _validate_multisig(msg.multisig, msg.transaction.version)
    if not msg.multisig and msg.cosigning:
        raise ProcessError("No multisig transaction to cosign")

    if msg.transfer:
        _validate_transfer(msg.transfer, msg.transaction.version)
    if(msg.namespace_registration):
        _validate_namespace_registration(msg.namespace_registration, msg.transaction.version)
    if(msg.address_alias):
        _validate_address_alias(msg.address_alias, msg.transaction.version)
    if msg.mosaic_alias:
        _validate_mosaic_alias(msg.mosaic_alias, msg.transaction.version)
    if msg.hash_lock:
        _validate_hash_lock(msg.hash_lock)

def _validate_single_tx(msg: NEM2SignTx):
    # ensure exactly one transaction is provided
    tx_count = (
        bool(msg.transfer)
        + bool(msg.namespace_registration)
        + bool(msg.mosaic_definition)
        + bool(msg.mosaic_supply)
        + bool(msg.address_alias)
        + bool(msg.mosaic_alias)
        + bool(msg.aggregate)
        + bool(msg.hash_lock)
        # + bool(msg.importance_transfer)
    )
    if tx_count == 0:
        raise ProcessError("No transaction provided")
    if tx_count > 1:
        raise ProcessError("More than one transaction provided")


def _validate_common(common: NEM2TransactionCommon, inner: bool = False):

    err = None
    if common.type is None:
        err = "type"
    if common.network_type is None:
        err = "network_type"
    if common.version is None:
        err = "version"
    if common.max_fee is None:
        err = "max_fee"
    if common.deadline is None:
        err = "deadline"

    if err:
        raise ProcessError("No %s provided" % err)


def _validate_multisig(multisig: NEM2TransactionCommon, version: int):
    if multisig.version != version:
        raise ProcessError("Inner transaction network is different")
    _validate_public_key(multisig.signer, "Invalid multisig signer public key provided")

def _validate_transfer(transfer: NEM2TransferTransaction, version: int):
    if transfer.recipient_address is None:
        raise ProcessError("No recipient provided")

    # TODO: replace C implementation of validate_address with something new for nem2
    # if not nem2.validate_address(transfer.recipient_address, network):
    #     raise ProcessError("Invalid recipient address")

    for m in transfer.mosaics:
        if m.id is None:
            raise ProcessError("No mosaic id provided")
        if m.amount is None:
            raise ProcessError("No mosaic amount provided")

def _validate_mosaic_alias(mosaic_alias: NEM2MosaicAliasTransaction, network: int):
    if mosaic_alias.namespace_id is None:
        raise ProcessError("No namespace ID provided")
    if mosaic_alias.mosaic_id is None:
        raise ProcessError("No mosiac ID provided")
    if mosaic_alias.alias_action is None:
        raise ProcessError("No alias action provided")

def _validate_hash_lock(hash_lock: NEM2HashLockTransaction):
    if hash_lock.mosaic is None:
        raise ProcessError("No mosaic provided")
    if hash_lock.duration is None:
        raise ProcessError("No duration provided")
    if hash_lock.hash is None:
        raise ProcessError("No AggregateTransaction hash provided")