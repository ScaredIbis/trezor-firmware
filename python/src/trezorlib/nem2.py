# This file is part of the Trezor project.
#
# Copyright (C) 2012-2019 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

import json

from . import messages as proto
from .tools import CallException, expect

TYPE_TRANSACTION_TRANSFER = 0x4154
TYPE_MULTISIG_SIGNATURE = 0x1002
TYPE_MOSAIC_DEFINITION = 0x414D
TYPE_MOSAIC_SUPPLY_CHANGE = 0x424D
TYPE_AGGREGATE_COMPLETE = 0x4141

NETWORK_TYPE_MIJIN_TEST = 0x90
NETWORK_TYPE_MIJIN = 0x60
NETWORK_TYPE_TEST_NET = 0x98
NETWORK_TYPE_MAIN_NET = 0x68

def create_transaction_common(transaction):
    msg = proto.NEM2TransactionCommon()
    msg.type = transaction["type"]
    msg.network_type = transaction["network_type"]
    msg.version = transaction["version"]
    msg.max_fee = transaction["max_fee"]
    msg.deadline = transaction["deadline"]

    if "signer" in transaction:
        msg.signer = bytes.fromhex(transaction["signer"])

    return msg


def create_transfer(transaction):
    msg = proto.NEM2TransferTransaction()
    msg.recipient_address = proto.NEM2RecipientAddress(
        address=transaction["recipient_address"]["address"],
        network_type=transaction["recipient_address"]["network_type"],
    )

    if "payload" in transaction["message"]:
        msg.message = proto.NEM2TransferMessage(
            payload=transaction["message"]["payload"],
            type=transaction["message"]["type"]
        )

    if "mosaics" in transaction:
        msg.mosaics = [
            proto.NEM2Mosaic(
                id=mosaic["id"],
                amount=mosaic["amount"],
            )
            for mosaic in transaction["mosaics"]
        ]

    return msg

def create_mosaic_defnition(transaction):
    msg = proto.NEM2MosaicDefinitionTransaction()
    msg.nonce = transaction["nonce"]
    msg.mosaic_id = transaction["mosaic_id"]
    msg.flags = transaction["flags"]
    msg.divisibility = transaction["divisibility"]
    msg.duration = int(transaction["duration"])
    return msg


def create_mosaic_supply(transaction):
    msg = proto.NEM2MosaicSupplyChangeTransaction()
    msg.mosaic_id = transaction["mosaic_id"]
    msg.delta = int(transaction["delta"])
    msg.action = transaction["action"]
    return msg

def fill_transaction_by_type(msg, transaction):
    if transaction["type"] == TYPE_TRANSACTION_TRANSFER:
        msg.transfer = create_transfer(transaction)
    if transaction["type"] == TYPE_MOSAIC_DEFINITION:
        msg.mosaic_definition = create_mosaic_defnition(transaction)
    if transaction["type"] == TYPE_MOSAIC_SUPPLY_CHANGE:
        msg.mosaic_supply = create_mosaic_supply(transaction)


def create_sign_tx(transaction):
    msg = proto.NEM2SignTx()
    msg.transaction = create_transaction_common(transaction)

    if transaction["type"] == TYPE_AGGREGATE_COMPLETE:
        inner_txs = []
        for tx in transaction["transactions"]:            
            embedded_tx = proto.NEM2EmbeddedTransaction()
            embedded_tx.transaction = create_transaction_common(tx["transaction"])
            fill_transaction_by_type(embedded_tx, tx["transaction"])
            inner_txs.append(embedded_tx)
        msg.aggregate_complete = proto.NEM2AggregateCompleteTransaction(inner_txs)
    else:
        fill_transaction_by_type(msg, transaction)

    return msg


# ====== Client functions ====== #


@expect(proto.NEMAddress, field="address")
def get_address(client, n, network, show_display=False):
    return client.call(
        proto.NEMGetAddress(address_n=n, network=network, show_display=show_display)
    )


@expect(proto.NEM2SignedTx)
def sign_tx(client, n, transaction):
    print("signing nem2 transaction")
    try:
        msg = create_sign_tx(transaction)
    except ValueError as e:
        raise CallException(e.args)

    assert msg.transaction is not None
    msg.address_n = n
    msg.generation_hash = transaction["generation_hash"]
    return client.call(msg)
