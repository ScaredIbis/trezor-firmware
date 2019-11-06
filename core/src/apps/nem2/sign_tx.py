from trezor.crypto.curve import ed25519
from trezor.messages.NEM2SignedTx import NEM2SignedTx
from trezor.messages.NEM2SignTx import NEM2SignTx

from apps.common import seed
from apps.common.paths import validate_path
from apps.nem2 import CURVE, transfer
from apps.nem2.helpers import NEM2_HASH_ALG, check_path
from apps.nem2.validators import validate


async def sign_tx(ctx, msg: NEM2SignTx, keychain):
    validate(msg)

    await validate_path(
        ctx,
        check_path,
        keychain,
        msg.address_n,
        CURVE,
    )

    node = keychain.derive(msg.address_n, CURVE)

    if msg.multisig:
        public_key = msg.multisig.signer
        common = msg.multisig
        await multisig.ask(ctx, msg)
    else:
        public_key = seed.remove_ed25519_prefix(node.public_key())
        common = msg.transaction

    if msg.transfer:
        tx = await transfer.transfer(ctx, public_key, common, msg.transfer, node)
    # elif msg.provision_namespace:
    #     tx = await namespace.namespace(ctx, public_key, common, msg.provision_namespace)
    # elif msg.mosaic_creation:
    #     tx = await mosaic.mosaic_creation(ctx, public_key, common, msg.mosaic_creation)
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
    else:
        raise ValueError("No transaction provided")

    if msg.multisig:
        # wrap transaction in multisig wrapper
        if msg.cosigning:
            tx = multisig.cosign(
                seed.remove_ed25519_prefix(node.public_key()),
                msg.transaction,
                tx,
                msg.multisig.signer,
            )
        else:
            tx = multisig.initiate(
                seed.remove_ed25519_prefix(node.public_key()), msg.transaction, tx
            )

    # https://nemtech.github.io/concepts/transaction.html#signing-a-transaction
    print("TX ", tx)
    # signature = ed25519.sign(node.private_key(), msg.generation_hash + tx.decode(), NEM2_HASH_ALG)
    # signature = ed25519.sign(node.private_key(), tx, NEM2_HASH_ALG)

    resp = NEM2SignedTx()
    resp.payload = "MOCK_PAYLOAD"
    resp.hash = "MOCK_HASH"
    return resp
