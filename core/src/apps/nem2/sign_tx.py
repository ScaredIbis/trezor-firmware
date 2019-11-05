from trezor.crypto.curve import ed25519
from trezor.messages.NEM2SignedTx import NEM2SignedTx
from trezor.messages.NEM2SignTx import NEM2SignTx

from apps.common import seed
from apps.common.paths import validate_path
from apps.nem2 import CURVE, transfer, mosaic
from apps.nem2.helpers import NEM_HASH_ALG, check_path
from apps.nem2.validators import validate


async def sign_tx(ctx, msg: NEM2SignTx, keychain):
    print("in sign_tx", check_path, msg.address_n)
    # validate(msg)

    await validate_path(
        ctx,
        check_path,
        keychain,
        msg.address_n,
        CURVE,
        network=msg.transaction.version,
    )

    node = keychain.derive(msg.address_n, CURVE)

    public_key = seed.remove_ed25519_prefix(node.public_key())
    common = msg.transaction

    print("type", msg.transfer, msg.mosaic_definition)
    if msg.transfer:
        tx = await transfer.transfer(ctx, public_key, common, msg.transfer, node)
    # elif msg.provision_namespace:
    #     tx = await namespace.namespace(ctx, public_key, common, msg.provision_namespace)
    elif msg.mosaic_definition:        
        tx = await mosaic.mosaic_definition(ctx, public_key, common, msg.mosaic_definition)
    # elif msg.supply_change:
    #     tx = await mosaic.supply_change(ctx, public_key, common, msg.supply_change)
    # elif msg.aggregate_modification:
    #     tx = await multisig.aggregate_modification(
    #         ctx,
    #         public_key,
    #         common,
    #         msg.aggregate_modification,
    #         msg.multisig is not None,
    #     )
    # elif msg.importance_transfer:
    #     tx = await transfer.importance_transfer(
    #         ctx, public_key, common, msg.importance_transfer
    #     )
    # else:
        raise ValueError("No transaction provided")

    # if msg.multisig:
    #     # wrap transaction in multisig wrapper
    #     if msg.cosigning:
    #         tx = multisig.cosign(
    #             seed.remove_ed25519_prefix(node.public_key()),
    #             msg.transaction,
    #             tx,
    #             msg.multisig.signer,
    #         )
    #     else:
    #         tx = multisig.initiate(
    #             seed.remove_ed25519_prefix(node.public_key()), msg.transaction, tx
    #         )

    print("signing", node.private_key(), tx)
    signature = ed25519.sign(node.private_key(), tx, NEM_HASH_ALG)

    resp = NEM2SignedTx()
    resp.data = tx
    resp.signature = signature
    return resp
