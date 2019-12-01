# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .NEM2MosaicDefinitionTransaction import NEM2MosaicDefinitionTransaction
from .NEM2MosaicSupplyChangeTransaction import NEM2MosaicSupplyChangeTransaction
from .NEM2TransactionCommon import NEM2TransactionCommon
from .NEM2TransferTransaction import NEM2TransferTransaction

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class NEM2EmbeddedTransaction(p.MessageType):

    def __init__(
        self,
        transaction: NEM2TransactionCommon = None,
        transfer: NEM2TransferTransaction = None,
        mosaic_definition: NEM2MosaicDefinitionTransaction = None,
        mosaic_supply: NEM2MosaicSupplyChangeTransaction = None,
    ) -> None:
        self.transaction = transaction
        self.transfer = transfer
        self.mosaic_definition = mosaic_definition
        self.mosaic_supply = mosaic_supply

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('transaction', NEM2TransactionCommon, 0),
            2: ('transfer', NEM2TransferTransaction, 0),
            3: ('mosaic_definition', NEM2MosaicDefinitionTransaction, 0),
            4: ('mosaic_supply', NEM2MosaicSupplyChangeTransaction, 0),
        }
