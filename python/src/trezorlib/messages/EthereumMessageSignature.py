# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class EthereumMessageSignature(p.MessageType):
    MESSAGE_WIRE_TYPE = 66

    def __init__(
        self,
        signature: bytes = None,
        address: str = None,
    ) -> None:
        self.signature = signature
        self.address = address

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            2: ('signature', p.BytesType, 0),
            3: ('address', p.UnicodeType, 0),
        }
