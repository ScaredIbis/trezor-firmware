# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
        EnumTypeNEM2EntityType = Literal[0, 16705, 16708, 16712, 16717, 16718, 16722, 16724, 16725, 16961, 16964, 16973, 16974, 16978, 17220, 17230]
        EnumTypeNEM2NetworkType = Literal[96, 104, 144, 152]
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore
        EnumTypeNEM2EntityType = None  # type: ignore
        EnumTypeNEM2NetworkType = None  # type: ignore


class NEM2EmbeddedTransactionCommon(p.MessageType):

    def __init__(
        self,
        type: EnumTypeNEM2EntityType = None,
        network_type: EnumTypeNEM2NetworkType = None,
        version: int = None,
        public_key: str = None,
    ) -> None:
        self.type = type
        self.network_type = network_type
        self.version = version
        self.public_key = public_key

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('type', p.EnumType("NEM2EntityType", (0, 16961, 16705, 17220, 16964, 16708, 16712, 16973, 16717, 16718, 16974, 17230, 16722, 16978, 16724, 16725)), 0),
            2: ('network_type', p.EnumType("NEM2NetworkType", (104, 144, 96, 152)), 0),
            3: ('version', p.UVarintType, 0),  # default=1
            4: ('public_key', p.UnicodeType, 0),
        }
