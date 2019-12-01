from trezor.messages.NEM2TransactionCommon import NEM2TransactionCommon
from trezor.messages.NEM2MosaicDefinitionTransaction import NEM2MosaicDefinitionTransaction
from trezor.messages.NEM2MosaicSupplyChangeTransaction import NEM2MosaicSupplyChangeTransaction

from . import layout, serialize

async def mosaic_definition(
    ctx,    
    common: NEM2TransactionCommon, 
    creation: NEM2MosaicDefinitionTransaction,
    embedded: bool
):
    await layout.ask_mosaic_definition(ctx, common, creation)
    return serialize.serialize_mosaic_definition(common, creation, embedded)

async def mosaic_supply(
    ctx, 
    common: NEM2TransactionCommon, 
    supply: NEM2MosaicSupplyChangeTransaction,
    embedded: bool
):
    # TODO: await layout.ask_mosaic_supply(ctx, common, supply)
    return serialize.serialize_mosaic_supply(common, supply, embedded)