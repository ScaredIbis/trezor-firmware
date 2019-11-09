# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .NEM2TransactionCommon import NEM2TransactionCommon
from .NEM2TransferTransaction import NEM2TransferTransaction

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
        EnumTypeNEM2NetworkType = Literal[96, 104, 144, 152]
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore
        EnumTypeNEM2NetworkType = None  # type: ignore


class NEM2SignTx(p.MessageType):
    MESSAGE_WIRE_TYPE = 806

    def __init__(
        self,
        transaction: NEM2TransactionCommon = None,
        multisig: NEM2TransactionCommon = None,
        transfer: NEM2TransferTransaction = None,
        generation_hash: str = None,
        network_type: EnumTypeNEM2NetworkType = None,
        address_n: List[int] = None,
        cosigning: bool = None,
    ) -> None:
        self.transaction = transaction
        self.multisig = multisig
        self.transfer = transfer
        self.generation_hash = generation_hash
        self.network_type = network_type
        self.address_n = address_n if address_n is not None else []
        self.cosigning = cosigning

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('transaction', NEM2TransactionCommon, 0),
            2: ('multisig', NEM2TransactionCommon, 0),
            3: ('transfer', NEM2TransferTransaction, 0),
            4: ('generation_hash', p.UnicodeType, 0),
            5: ('network_type', p.EnumType("NEM2NetworkType", (104, 144, 96, 152)), 0),  # default=MAIN_NET
            6: ('address_n', p.UVarintType, p.FLAG_REPEATED),
            7: ('cosigning', p.BoolType, 0),
        }
