# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .NEM2AggregateTransaction import NEM2AggregateTransaction
from .NEM2MosaicDefinitionTransaction import NEM2MosaicDefinitionTransaction
from .NEM2MosaicSupplyChangeTransaction import NEM2MosaicSupplyChangeTransaction
from .NEM2NamespaceMetadataTransaction import NEM2NamespaceMetadataTransaction
from .NEM2NamespaceRegistrationTransaction import NEM2NamespaceRegistrationTransaction
from .NEM2TransactionCommon import NEM2TransactionCommon
from .NEM2TransferTransaction import NEM2TransferTransaction

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class NEM2SignTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 806

    def __init__(
        self,
        transaction: NEM2TransactionCommon = None,
        multisig: NEM2TransactionCommon = None,
        transfer: NEM2TransferTransaction = None,
        generation_hash: str = None,
        address_n: List[int] = None,
        cosigning: bool = None,
        mosaic_definition: NEM2MosaicDefinitionTransaction = None,
        mosaic_supply: NEM2MosaicSupplyChangeTransaction = None,
        aggregate: NEM2AggregateTransaction = None,
        namespace_metadata: NEM2NamespaceMetadataTransaction = None,
    ) -> None:
        self.transaction = transaction
        self.multisig = multisig
        self.transfer = transfer
        self.generation_hash = generation_hash
        self.address_n = address_n if address_n is not None else []
        self.cosigning = cosigning
        self.mosaic_definition = mosaic_definition
        self.mosaic_supply = mosaic_supply
        self.aggregate = aggregate
        self.namespace_metadata = namespace_metadata

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('transaction', NEM2TransactionCommon, 0),
            2: ('multisig', NEM2TransactionCommon, 0),
            3: ('transfer', NEM2TransferTransaction, 0),
            4: ('generation_hash', p.UnicodeType, 0),
            5: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            6: ('cosigning', p.BoolType, 0),
            7: ('mosaic_definition', NEM2MosaicDefinitionTransaction, 0),
            8: ('mosaic_supply', NEM2MosaicSupplyChangeTransaction, 0),
            9: ('namespace_registration', NEM2NamespaceRegistrationTransaction, 0),
            10: ('address_alias', NEM2AddressAliasTransaction, 0),
            11: ('aggregate', NEM2AggregateTransaction, 0),
            12: ('namespace_metadata', NEM2NamespaceMetadataTransaction, 0),
        }
