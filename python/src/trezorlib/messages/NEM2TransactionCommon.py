# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
        EnumTypeNEM2EntityType = Literal[0, 16717, 16718, 16724, 16973, 16974]
        EnumTypeNEM2NetworkType = Literal[96, 104, 144, 152]
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore
        EnumTypeNEM2EntityType = None  # type: ignore
        EnumTypeNEM2NetworkType = None  # type: ignore


class NEM2TransactionCommon(p.MessageType):

    def __init__(
        self,
        type: EnumTypeNEM2EntityType = None,
        network_type: EnumTypeNEM2NetworkType = None,
        version: int = None,
        max_fee: str = None,
        deadline: str = None,
    ) -> None:
        self.type = type
        self.network_type = network_type
        self.version = version
        self.max_fee = max_fee
        self.deadline = deadline

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('type', p.EnumType("NEM2EntityType", (0, 16973, 16717, 16718, 16974, 16724)), 0),
            2: ('network_type', p.EnumType("NEM2NetworkType", (104, 144, 96, 152)), 0),
            3: ('version', p.UVarintType, 0),  # default=1
            4: ('max_fee', p.UnicodeType, 0),
            5: ('deadline', p.UnicodeType, 0),
        }
