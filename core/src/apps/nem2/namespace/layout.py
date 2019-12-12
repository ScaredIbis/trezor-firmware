from trezor import ui

from trezor.messages import ButtonRequestType
from trezor.messages.NEM2TransactionCommon import NEM2TransactionCommon
from trezor.messages.NEM2EmbeddedTransactionCommon import NEM2EmbeddedTransactionCommon
from trezor.messages.NEM2NamespaceRegistrationTransaction import NEM2NamespaceRegistrationTransaction
from trezor.messages.NEM2AddressAliasTransaction import NEM2AddressAliasTransaction
from trezor.messages.NEM2MosaicAliasTransaction import NEM2MosaicAliasTransaction

from trezor.ui.text import Text
from trezor.ui.scroll import Paginated

from ..helpers import (
    NEM2_NAMESPACE_REGISTRATION_TYPE_ROOT,
    NEM2_NAMESPACE_REGISTRATION_TYPE_SUB,
    NEM2_ALIAS_ACTION_TYPE_LINK,
    NEM2_ALIAS_ACTION_TYPE_UNLINK,
)
from ..layout import require_confirm_final

from apps.common.confirm import require_confirm
from apps.common.layout import split_address

async def ask_namespace_registration(
    ctx,
    common: NEM2TransactionCommon | NEM2EmbeddedTransactionCommon,
    namespace_registration: NEM2NamespaceRegistrationTransaction,
    embedded=False
):
    # confirm name and id
    msg = Text("Register Namespace")
    msg.normal("Id:")
    msg.bold(namespace_registration.id.upper())
    msg.normal("Name:")
    msg.bold(namespace_registration.namespace_name)
    await require_confirm(ctx, msg, ButtonRequestType.ConfirmOutput)

    # confirm registration type and either parentId and  and id
    msg = Text("Register Namespace")
    msg.normal("Registration Type:")
    if(namespace_registration.registration_type == NEM2_NAMESPACE_REGISTRATION_TYPE_ROOT):
        msg.bold("Root Namespace")
        msg.normal("Duration:")
        msg.bold(namespace_registration.duration)
    elif (namespace_registration.registration_type == NEM2_NAMESPACE_REGISTRATION_TYPE_SUB):
        msg.bold("Sub Namespace")
        msg.normal("Parent Id:")
        msg.bold(namespace_registration.parent_id.upper())
    await require_confirm(ctx, msg, ButtonRequestType.ConfirmOutput)

    if not embedded:
        await require_confirm_final(ctx, common.max_fee)

async def ask_address_alias(
    ctx,
    common: NEM2TransactionCommon | NEM2EmbeddedTransactionCommon,
    address_alias: NEM2NamespaceRegistrationTransaction,
    embedded=False
):
    # confirm namespace id
    msg = Text("Address Alias")
    msg.normal("Namspace Id:")
    msg.bold(address_alias.namespace_id.upper())
    msg.normal("Alias Action:")
    if(address_alias.alias_action == NEM2_ALIAS_ACTION_TYPE_LINK):
        msg.bold("LINK")
    elif (address_alias.alias_action == NEM2_ALIAS_ACTION_TYPE_UNLINK):
        msg.bold("UNLINK")
    await require_confirm(ctx, msg, ButtonRequestType.ConfirmOutput)

    # confirm address to link/unlink
    msg = Text("Address Alias", ui.ICON_SEND, ui.GREEN)
    msg.normal("Address:")
    msg.mono(*split_address(address_alias.address.address))
    await require_confirm(ctx, msg, ButtonRequestType.ConfirmOutput)

    if not embedded:
        await require_confirm_final(ctx, common.max_fee)

async def ask_mosaic_alias(
    ctx,
    common: NEM2TransactionCommon | NEM2EmbeddedTransactionCommon,
    mosaic_alias: NEM2MosaicAliasTransaction,
    embedded=False
):
    await require_confirm_properties(ctx, mosaic_alias)
    if not embedded:
        await require_confirm_final(ctx, common.max_fee)

async def require_confirm_properties(ctx, mosaic_alias: NEM2MosaicAliasTransaction):
    properties = []

    # Mosaic ID
    if mosaic_alias.mosaic_id:
        t = Text("Confirm properties", ui.ICON_SEND, new_lines=False)
        t.bold("Mosaic Id:")
        t.br()
        t.normal(mosaic_alias.mosaic_id)
        properties.append(t)

    # Namespace ID
    if mosaic_alias.namespace_id:
        t = Text("Confirm properties", ui.ICON_SEND, new_lines=False)
        t.bold("Namespace Id:")
        t.br()
        t.normal(mosaic_alias.namespace_id)
        properties.append(t)
    # Alias Action
    if (mosaic_alias.alias_action == NEM2_ALIAS_ACTION_TYPE_LINK or 
        mosaic_alias.alias_action == NEM2_ALIAS_ACTION_TYPE_UNLINK):
        alias_text = "Link" if mosaic_alias.alias_action else "Unlink"
        t = Text("Confirm properties", ui.ICON_SEND, new_lines=False)
        t.bold("Alias Action:")
        t.br()
        t.normal('{} ({})'.format(alias_text, mosaic_alias.alias_action))
        properties.append(t)

    paginated = Paginated(properties)
    await require_confirm(ctx, paginated, ButtonRequestType.ConfirmOutput)
