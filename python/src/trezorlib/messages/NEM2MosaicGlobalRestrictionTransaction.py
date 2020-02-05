# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List  # noqa: F401
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        pass


class NEM2MosaicGlobalRestrictionTransaction(p.MessageType):

    def __init__(
        self,
        mosaic_id: str = None,
        reference_mosaic_id: str = None,
        restriction_key: str = None,
        previous_restriction_value: str = None,
        new_restriction_value: str = None,
        previous_restriction_type: int = None,
        new_restriction_type: int = None,
    ) -> None:
        self.mosaic_id = mosaic_id
        self.reference_mosaic_id = reference_mosaic_id
        self.restriction_key = restriction_key
        self.previous_restriction_value = previous_restriction_value
        self.new_restriction_value = new_restriction_value
        self.previous_restriction_type = previous_restriction_type
        self.new_restriction_type = new_restriction_type

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('mosaic_id', p.UnicodeType, 0),
            2: ('reference_mosaic_id', p.UnicodeType, 0),
            3: ('restriction_key', p.UnicodeType, 0),
            4: ('previous_restriction_value', p.UnicodeType, 0),
            5: ('new_restriction_value', p.UnicodeType, 0),
            6: ('previous_restriction_type', p.UVarintType, 0),
            7: ('new_restriction_type', p.UVarintType, 0),
        }