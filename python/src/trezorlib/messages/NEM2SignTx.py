# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .NEM2AccountMetadataTransaction import NEM2AccountMetadataTransaction
from .NEM2AddressAliasTransaction import NEM2AddressAliasTransaction
from .NEM2AggregateTransaction import NEM2AggregateTransaction
from .NEM2HashLockTransaction import NEM2HashLockTransaction
from .NEM2MosaicAliasTransaction import NEM2MosaicAliasTransaction
from .NEM2MosaicDefinitionTransaction import NEM2MosaicDefinitionTransaction
from .NEM2MosaicMetadataTransaction import NEM2MosaicMetadataTransaction
from .NEM2MosaicSupplyChangeTransaction import NEM2MosaicSupplyChangeTransaction
from .NEM2NamespaceMetadataTransaction import NEM2NamespaceMetadataTransaction
from .NEM2NamespaceRegistrationTransaction import NEM2NamespaceRegistrationTransaction
from .NEM2SecretLockTransaction import NEM2SecretLockTransaction
from .NEM2SecretProofTransaction import NEM2SecretProofTransaction
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
        namespace_registration: NEM2NamespaceRegistrationTransaction = None,
        address_alias: NEM2AddressAliasTransaction = None,
        aggregate: NEM2AggregateTransaction = None,
        namespace_metadata: NEM2NamespaceMetadataTransaction = None,
        mosaic_metadata: NEM2MosaicMetadataTransaction = None,
        account_metadata: NEM2AccountMetadataTransaction = None,
        mosaic_alias: NEM2MosaicAliasTransaction = None,
        hash_lock: NEM2HashLockTransaction = None,
        secret_lock: NEM2SecretLockTransaction = None,
        secret_proof: NEM2SecretProofTransaction = None,
    ) -> None:
        self.transaction = transaction
        self.multisig = multisig
        self.transfer = transfer
        self.generation_hash = generation_hash
        self.address_n = address_n if address_n is not None else []
        self.cosigning = cosigning
        self.mosaic_definition = mosaic_definition
        self.mosaic_supply = mosaic_supply
        self.namespace_registration = namespace_registration
        self.address_alias = address_alias
        self.aggregate = aggregate
        self.namespace_metadata = namespace_metadata
        self.mosaic_metadata = mosaic_metadata
        self.account_metadata = account_metadata
        self.mosaic_alias = mosaic_alias
        self.hash_lock = hash_lock
        self.secret_lock = secret_lock
        self.secret_proof = secret_proof

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
            13: ('mosaic_metadata', NEM2MosaicMetadataTransaction, 0),
            14: ('account_metadata', NEM2AccountMetadataTransaction, 0),
            15: ('mosaic_alias', NEM2MosaicAliasTransaction, 0),
            16: ('hash_lock', NEM2HashLockTransaction, 0),
            17: ('secret_lock', NEM2SecretLockTransaction, 0),
            18: ('secret_proof', NEM2SecretProofTransaction, 0),
        }
