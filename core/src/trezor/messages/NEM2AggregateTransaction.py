# Automatically generated by pb2py
# fmt: off
import protobuf as p

from .NEM2Cosignature import NEM2Cosignature
from .NEM2InnerTransaction import NEM2InnerTransaction

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class NEM2AggregateTransaction(p.MessageType):

    def __init__(
        self,
        inner_transactions: List[NEM2InnerTransaction] = None,
        cosignatures: List[NEM2Cosignature] = None,
    ) -> None:
        self.inner_transactions = inner_transactions if inner_transactions is not None else []
        self.cosignatures = cosignatures if cosignatures is not None else []

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('inner_transactions', NEM2InnerTransaction, p.FLAG_REPEATED),
            2: ('cosignatures', NEM2Cosignature, p.FLAG_REPEATED),
        }