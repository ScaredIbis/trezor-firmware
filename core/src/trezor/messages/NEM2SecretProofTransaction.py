# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .NEM2Address import NEM2Address

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeNEM2LockHashAlgorithm = Literal[0, 1, 2, 3]
    except ImportError:
        pass


class NEM2SecretProofTransaction(p.MessageType):

    def __init__(
        self,
        secret: str = None,
        hash_algorithm: EnumTypeNEM2LockHashAlgorithm = None,
        recipient_address: NEM2Address = None,
        proof: str = None,
    ) -> None:
        self.secret = secret
        self.hash_algorithm = hash_algorithm
        self.recipient_address = recipient_address
        self.proof = proof

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('secret', p.UnicodeType, 0),
            2: ('hash_algorithm', p.EnumType("NEM2LockHashAlgorithm", (0, 1, 2, 3)), 0),  # default=SHA3_256
            3: ('recipient_address', NEM2Address, 0),
            4: ('proof', p.UnicodeType, 0),
        }
