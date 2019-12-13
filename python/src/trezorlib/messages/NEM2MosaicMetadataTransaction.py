# Automatically generated by pb2py
# fmt: off
from .. import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore


class NEM2MosaicMetadataTransaction(p.MessageType):

    def __init__(
        self,
        target_public_key: str = None,
        scoped_metadata_key: str = None,
        target_mosaic_id: str = None,
        value_size_delta: int = None,
        value_size: int = None,
        value: str = None,
    ) -> None:
        self.target_public_key = target_public_key
        self.scoped_metadata_key = scoped_metadata_key
        self.target_mosaic_id = target_mosaic_id
        self.value_size_delta = value_size_delta
        self.value_size = value_size
        self.value = value

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('target_public_key', p.UnicodeType, 0),
            2: ('scoped_metadata_key', p.UnicodeType, 0),
            3: ('target_mosaic_id', p.UnicodeType, 0),
            4: ('value_size_delta', p.UVarintType, 0),
            5: ('value_size', p.UVarintType, 0),
            6: ('value', p.UnicodeType, 0),
        }
