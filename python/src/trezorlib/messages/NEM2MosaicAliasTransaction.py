# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
        EnumTypeNEM2AliasAction = Literal[0, 1]
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore
        EnumTypeNEM2AliasAction = None  # type: ignore


class NEM2MosaicAliasTransaction(p.MessageType):

    def __init__(
        self,
        alias_action: EnumTypeNEM2AliasAction = None,
        namespace_id: str = None,
        mosaic_id: str = None,
    ) -> None:
        self.alias_action = alias_action
        self.namespace_id = namespace_id
        self.mosaic_id = mosaic_id

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('alias_action', p.EnumType("NEM2AliasAction", (0, 1)), 0),  # default=LINK
            2: ('namespace_id', p.UnicodeType, 0),
            3: ('mosaic_id', p.UnicodeType, 0),
        }
