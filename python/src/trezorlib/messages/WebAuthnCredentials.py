# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

from .WebAuthnCredential import WebAuthnCredential

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class WebAuthnCredentials(p.MessageType):
    MESSAGE_WIRE_TYPE = 801

    def __init__(
        self,
        credentials: List[WebAuthnCredential] = None,
    ) -> None:
        self.credentials = credentials if credentials is not None else []

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('credentials', WebAuthnCredential, p.FLAG_REPEATED),
        }
