from trezor.messages.NEM2TransactionCommon import NEM2TransactionCommon
from trezor.messages.NEM2NamespaceMetadataTransaction import NEM2NamespaceMetadataTransaction
from trezor.messages.NEM2MosaicMetadataTransaction import NEM2MosaicMetadataTransaction
from trezor.messages.NEM2AccountMetadataTransaction import NEM2AccountMetadataTransaction

from . import layout, serialize

async def metadata(
    ctx,
    common: NEM2TransactionCommon,
    metadata: NEM2NamespaceMetadataTransaction | NEM2MosaicMetadataTransaction | NEM2AccountMetadataTransaction
):
    await layout.ask_metadata(ctx, common, metadata)
    return serialize.serialize_metadata(common, metadata)