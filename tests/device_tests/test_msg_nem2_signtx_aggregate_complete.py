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

import pytest

from trezorlib import nem2
from trezorlib.tools import parse_path

from ..common import MNEMONIC12

@pytest.mark.altcoin
@pytest.mark.nem2
class TestMsgNEM2SignTxAggregateComplete:
    @pytest.mark.setup_client(mnemonic=MNEMONIC12)
    def test_nem2_signtx_aggregate_complete_mosaic(self, client):
        tx = nem2.sign_tx(
            client,
            parse_path("m/44'/43'/0'/0'/0'"),
            {
                "type": nem2.TYPE_AGGREGATE_COMPLETE,
                "network_type": nem2.NETWORK_TYPE_TEST_NET,
                "generation_hash": "9F1979BEBA29C47E59B40393ABB516801A353CFC0C18BC241FEDE41939C907E7",
                "version": 38913,
                "max_fee": "100",
                "deadline": "113728610090",
                "transactions": [
                    {
                        "transaction": {
                            "type": nem2.TYPE_MOSAIC_DEFINITION,
                            "network_type": nem2.NETWORK_TYPE_TEST_NET,
                            "generation_hash": "9F1979BEBA29C47E59B40393ABB516801A353CFC0C18BC241FEDE41939C907E7",
                            "version": 38913,
                            "max_fee": "100",
                            "deadline": "113728610090",
                            "nonce": 3095715558,
                            "mosaic_id": "0B65C4B29A80C619",
                            "flags": 7,
                            "divisibility": 100,
                            "duration": "123"
                        },
                    },
                    {
                        "transaction": {
                            "type": nem2.TYPE_MOSAIC_SUPPLY_CHANGE,
                            "network_type": nem2.NETWORK_TYPE_TEST_NET,
                            "generation_hash": "9F1979BEBA29C47E59B40393ABB516801A353CFC0C18BC241FEDE41939C907E7",
                            "version": 38913,
                            "max_fee": "100",
                            "deadline": "113728610090",
                            "mosaic_id": "0B65C4B29A80C619",
                            "action": 1,
                            "delta": "1000000"
                        }
                    }
                ]
            },
        )

        print(tx.payload.hex().upper())        

        assert (
            tx.payload.hex().upper()
            == "380100000000000082D60BC7FCB805742CDDACE037DE4AC2193FCEDB949F77D81377F0542AC88CF845FA775808165CF276B83C9858BE3887C7338C1E815B6699B7900FC078319B0BA8F70E4D5C357273968B12417AE8B742E35E530623C2488D0A73306B41271500000000000198414164000000000000002ADFC07A1A0000002606CFDACBD40E2FAFCEA7F1B797DB264993C4E24EF935A4571772A42C53D0F890000000000000004600000000000000A8F70E4D5C357273968B12417AE8B742E35E530623C2488D0A73306B412715000000000001984D4119C6809AB2C4650B7B00000000000000E6DE84B8076400004100000000000000A8F70E4D5C357273968B12417AE8B742E35E530623C2488D0A73306B412715000000000001984D4219C6809AB2C4650B40420F00000000000100000000000000"
        )
        assert (
            tx.hash.hex().upper()
            == "43FBE7E4061534E58F60D4E86033C0FC3477AC9E6FB06148D7F12AE9F33466C9"
        )