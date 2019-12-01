from trezor.messages.NEM2TransactionCommon import NEM2TransactionCommon
from trezor.messages.NEM2AggregateCompleteTransaction import NEM2AggregateCompleteTransaction

from ..writers import (
    serialize_tx_common,
    get_common_message_size,    
    write_uint32_le,
    write_uint32_be,
    write_uint64_le,
    write_uint8
)

def serialize_aggregate_complete(
    common: NEM2TransactionCommon, 
    aggregate: NEM2AggregateCompleteTransaction,
    transactions_size: int
):
    tx = bytearray()

    size = get_common_message_size()
    # add up the aggregate specific message attribute sizes
    size += 32 # transaction hash
    size += 4 # payload size
    size += 4 # header reserved
    size += transactions_size  

    write_uint32_le(tx, size)

    tx = serialize_tx_common(tx, common)    

    return tx
