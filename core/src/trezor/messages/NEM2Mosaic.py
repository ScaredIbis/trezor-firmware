# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class NEM2Mosaic(p.MessageType):

    def __init__(
        self,
        id: str = None,
        amount: str = None,
    ) -> None:
        self.id = id
        self.amount = amount

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('id', p.UnicodeType, 0),
            2: ('amount', p.UnicodeType, 0),
        }
