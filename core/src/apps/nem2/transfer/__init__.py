from trezor.messages.NEM2TransactionCommon import NEM2TransactionCommon
from trezor.messages.NEM2TransferTransaction import NEM2TransferTransaction

from . import layout, serialize

async def transfer(
    ctx, 
    public_key: bytes, 
    common: NEM2TransactionCommon, 
    transfer: NEM2TransferTransaction,
    embedded: bool   
):
    transfer.mosaics = serialize.canonicalize_mosaics(transfer.mosaics)

    await layout.ask_transfer(ctx, common, transfer)

    w, size = serialize.serialize_transfer(common, transfer, embedded)
    for mosaic in transfer.mosaics:
        serialize.serialize_mosaic(w, mosaic.id, mosaic.amount)
    return w, size