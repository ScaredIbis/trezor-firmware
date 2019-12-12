# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
        EnumTypeNEM2MosaicSupplyChangeAction = Literal[0, 1]
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore
        EnumTypeNEM2MosaicSupplyChangeAction = None  # type: ignore


class NEM2MosaicSupplyChangeTransaction(p.MessageType):

    def __init__(
        self,
        mosaic_id: str = None,
        action: EnumTypeNEM2MosaicSupplyChangeAction = None,
        delta: int = None,
    ) -> None:
        self.mosaic_id = mosaic_id
        self.action = action
        self.delta = delta

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('mosaic_id', p.UnicodeType, 0),
            2: ('action', p.EnumType("NEM2MosaicSupplyChangeAction", (0, 1)), 0),  # default=INCREASE
            3: ('delta', p.UVarintType, 0),
        }
