from trezor.messages.NEM2SignTx import (
    NEM2SignTx,
    NEM2TransactionCommon,
    NEM2TransferTransaction,
)
from trezor.wire import ProcessError

from .helpers import (
    NEM_MAX_DIVISIBILITY,
    NEM_MAX_ENCRYPTED_PAYLOAD_SIZE,
    NEM_MAX_PLAIN_PAYLOAD_SIZE,
    NEM_MAX_SUPPLY,
    NEM_NETWORK_MAINNET,
    NEM_NETWORK_MIJIN,
    NEM_NETWORK_TESTNET,
    NEM_PUBLIC_KEY_SIZE,
)

def validate(msg: NEMSignTx):
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



def _validate_single_tx(msg: NEMSignTx):
    # ensure exactly one transaction is provided
    tx_count = (
        bool(msg.transfer)
        # + bool(msg.provision_namespace)
        # + bool(msg.mosaic_creation)
        # + bool(msg.supply_change)
        # + bool(msg.aggregate_modification)
        # + bool(msg.importance_transfer)
    )
    if tx_count == 0:
        raise ProcessError("No transaction provided")
    if tx_count > 1:
        raise ProcessError("More than one transaction provided")


def _validate_common(common: NEM2TransactionCommon, inner: bool = False):

    print("VALIDATING COMMON", common)
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


def _validate_multisig(multisig: NEMTransactionCommon, network: int):
    if multisig.network != network:
        raise ProcessError("Inner transaction network is different")
    _validate_public_key(multisig.signer, "Invalid multisig signer public key provided")

def _validate_transfer(transfer: NEMTransfer, network: int):
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
