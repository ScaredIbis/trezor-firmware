# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
        EnumTypeNEM2AliasAction = Literal[0, 1]
    except ImportError:
        pass


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
            1: ('alias_action', p.EnumType("NEM2AliasAction", (1, 0)), 0),  # default=LINK
            2: ('namespace_id', p.UnicodeType, 0),
            3: ('mosaic_id', p.UnicodeType, 0),
        }
