from trezor.messages.NEM2TransactionCommon import NEM2TransactionCommon
from trezor.messages.NEM2AggregateCompleteTransaction import NEM2AggregateCompleteTransaction

from . import serialize

async def aggregate_complete(
    ctx,    
    common: NEM2TransactionCommon, 
    aggregate: NEM2AggregateCompleteTransaction,
    transactions_size: int
) -> bytearray:
    # await layout.ask_aggregate_complete(ctx, common, aggregate)
    return serialize.serialize_aggregate_complete(common, aggregate, transactions_size)
