# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .NEM2Mosaic import NEM2Mosaic

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class NEM2TransferTransaction(p.MessageType):

    def __init__(
        self,
        recipient_address: str = None,
        message: bytes = None,
        mosaics: List[NEM2Mosaic] = None,
    ) -> None:
        self.recipient_address = recipient_address
        self.message = message
        self.mosaics = mosaics if mosaics is not None else []

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('recipient_address', p.UnicodeType, 0),
            2: ('message', p.BytesType, 0),
            3: ('mosaics', NEM2Mosaic, p.FLAG_REPEATED),
        }