# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .NEM2AccountAddressRestrictionTransaction import NEM2AccountAddressRestrictionTransaction
from .NEM2AccountLinkTransaction import NEM2AccountLinkTransaction
from .NEM2AccountMetadataTransaction import NEM2AccountMetadataTransaction
from .NEM2AccountMosaicRestrictionTransaction import NEM2AccountMosaicRestrictionTransaction
from .NEM2AccountOperationRestrictionTransaction import NEM2AccountOperationRestrictionTransaction
from .NEM2AddressAliasTransaction import NEM2AddressAliasTransaction
from .NEM2EmbeddedTransactionCommon import NEM2EmbeddedTransactionCommon
from .NEM2HashLockTransaction import NEM2HashLockTransaction
from .NEM2MosaicAddressRestrictionTransaction import NEM2MosaicAddressRestrictionTransaction
from .NEM2MosaicAliasTransaction import NEM2MosaicAliasTransaction
from .NEM2MosaicDefinitionTransaction import NEM2MosaicDefinitionTransaction
from .NEM2MosaicGlobalRestrictionTransaction import NEM2MosaicGlobalRestrictionTransaction
from .NEM2MosaicMetadataTransaction import NEM2MosaicMetadataTransaction
from .NEM2MosaicSupplyChangeTransaction import NEM2MosaicSupplyChangeTransaction
from .NEM2MultisigModificationTransaction import NEM2MultisigModificationTransaction
from .NEM2NamespaceMetadataTransaction import NEM2NamespaceMetadataTransaction
from .NEM2NamespaceRegistrationTransaction import NEM2NamespaceRegistrationTransaction
from .NEM2SecretLockTransaction import NEM2SecretLockTransaction
from .NEM2SecretProofTransaction import NEM2SecretProofTransaction
from .NEM2TransferTransaction import NEM2TransferTransaction

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEM2InnerTransaction(p.MessageType):

    def __init__(
        self,
        common: NEM2EmbeddedTransactionCommon = None,
        transfer: NEM2TransferTransaction = None,
        mosaic_definition: NEM2MosaicDefinitionTransaction = None,
        mosaic_supply: NEM2MosaicSupplyChangeTransaction = None,
        namespace_registration: NEM2NamespaceRegistrationTransaction = None,
        address_alias: NEM2AddressAliasTransaction = None,
        mosaic_alias: NEM2MosaicAliasTransaction = None,
        hash_lock: NEM2HashLockTransaction = None,
        secret_lock: NEM2SecretLockTransaction = None,
        secret_proof: NEM2SecretProofTransaction = None,
        namespace_metadata: NEM2NamespaceMetadataTransaction = None,
        mosaic_metadata: NEM2MosaicMetadataTransaction = None,
        account_metadata: NEM2AccountMetadataTransaction = None,
        multisig_modification: NEM2MultisigModificationTransaction = None,
        account_address_restriction: NEM2AccountAddressRestrictionTransaction = None,
        account_mosaic_restriction: NEM2AccountMosaicRestrictionTransaction = None,
        account_operation_restriction: NEM2AccountOperationRestrictionTransaction = None,
        account_link: NEM2AccountLinkTransaction = None,
        mosaic_global_restriction: NEM2MosaicGlobalRestrictionTransaction = None,
        mosaic_address_restriction: NEM2MosaicAddressRestrictionTransaction = None,
    ) -> None:
        self.common = common
        self.transfer = transfer
        self.mosaic_definition = mosaic_definition
        self.mosaic_supply = mosaic_supply
        self.namespace_registration = namespace_registration
        self.address_alias = address_alias
        self.mosaic_alias = mosaic_alias
        self.hash_lock = hash_lock
        self.secret_lock = secret_lock
        self.secret_proof = secret_proof
        self.namespace_metadata = namespace_metadata
        self.mosaic_metadata = mosaic_metadata
        self.account_metadata = account_metadata
        self.multisig_modification = multisig_modification
        self.account_address_restriction = account_address_restriction
        self.account_mosaic_restriction = account_mosaic_restriction
        self.account_operation_restriction = account_operation_restriction
        self.account_link = account_link
        self.mosaic_global_restriction = mosaic_global_restriction
        self.mosaic_address_restriction = mosaic_address_restriction

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('common', NEM2EmbeddedTransactionCommon, 0),
            2: ('transfer', NEM2TransferTransaction, 0),
            3: ('mosaic_definition', NEM2MosaicDefinitionTransaction, 0),
            4: ('mosaic_supply', NEM2MosaicSupplyChangeTransaction, 0),
            5: ('namespace_registration', NEM2NamespaceRegistrationTransaction, 0),
            6: ('address_alias', NEM2AddressAliasTransaction, 0),
            7: ('mosaic_alias', NEM2MosaicAliasTransaction, 0),
            8: ('hash_lock', NEM2HashLockTransaction, 0),
            9: ('secret_lock', NEM2SecretLockTransaction, 0),
            10: ('secret_proof', NEM2SecretProofTransaction, 0),
            11: ('namespace_metadata', NEM2NamespaceMetadataTransaction, 0),
            12: ('mosaic_metadata', NEM2MosaicMetadataTransaction, 0),
            13: ('account_metadata', NEM2AccountMetadataTransaction, 0),
            14: ('multisig_modification', NEM2MultisigModificationTransaction, 0),
            15: ('account_address_restriction', NEM2AccountAddressRestrictionTransaction, 0),
            16: ('account_mosaic_restriction', NEM2AccountMosaicRestrictionTransaction, 0),
            17: ('account_operation_restriction', NEM2AccountOperationRestrictionTransaction, 0),
            18: ('account_link', NEM2AccountLinkTransaction, 0),
            19: ('mosaic_global_restriction', NEM2MosaicGlobalRestrictionTransaction, 0),
            20: ('mosaic_address_restriction', NEM2MosaicAddressRestrictionTransaction, 0),
        }
