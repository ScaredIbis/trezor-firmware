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

NETWORK_TEST_NET = 152


def create_transaction_common(transaction):
    msg = proto.NEM2TransactionCommon()    
    msg.max_fee = int(transaction["maxFee"])
    msg.deadline = transaction["deadline"]
    msg.networkType = transaction["networkType"]
    msg.version = transaction["version"]
    return msg


def create_transfer(transaction):
    msg = proto.NEM2TransferTransaction()
    msg.recipient_address = transaction["recipient_address"]
    msg.amount = transaction["amount"]

    if "payload" in transaction["message"]:
        msg.message = bytes.fromhex(transaction["message"]["payload"])

        if transaction["message"]["type"] == 0x02:
            msg.public_key = bytes.fromhex(transaction["message"]["publicKey"])

    if "mosaics" in transaction:
        msg.mosaics = [
            proto.NEMMosaic(
                namespace=mosaic["mosaicId"]["namespaceId"],
                mosaic=mosaic["mosaicId"]["name"],
                quantity=mosaic["quantity"],
            )
            for mosaic in transaction["mosaics"]
        ]

    return msg

def create_mosaic_defnition(transaction):
    msg = proto.NEM2MosaicDefinitionTransaction()
    return msg

def fill_transaction_by_type(msg, transaction):
    if transaction["type"] == TYPE_TRANSACTION_TRANSFER:
        msg.transfer = create_transfer(transaction)
    if transaction["type"] == TYPE_MOSAIC_DEFINITION:
        msg.mosaic_definition = create_mosaic_defnition(transaction)
    else:
        raise ValueError("Unknown transaction type")


def create_sign_tx(transaction):
    msg = proto.NEM2SignTx()
    msg.transaction = create_transaction_common(transaction)

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
    try:
        msg = create_sign_tx(transaction)
    except ValueError as e:
        raise CallException(e.args)

    print("GOT TO HERE", msg)
    msg.address_n = n
    return client.call(msg)
