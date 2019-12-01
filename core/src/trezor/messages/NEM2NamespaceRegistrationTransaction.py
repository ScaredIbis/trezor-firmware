# Automatically generated by pb2py
# fmt: off
import protobuf as p

if __debug__:
    try:
        from typing import Dict, List, Optional
        from typing_extensions import Literal  # noqa: F401
        EnumTypeNEM2NamespaceRegistrationType = Literal[0, 1]
    except ImportError:
        Dict, List, Optional = None, None, None  # type: ignore
        EnumTypeNEM2NamespaceRegistrationType = None  # type: ignore


class NEM2NamespaceRegistrationTransaction(p.MessageType):

    def __init__(
        self,
        duration: int = None,
        parent_id: int = None,
        id: int = None,
        registration_type: EnumTypeNEM2NamespaceRegistrationType = None,
        name_size: int = None,
        namespace_name: bytes = None,
    ) -> None:
        self.duration = duration
        self.parent_id = parent_id
        self.id = id
        self.registration_type = registration_type
        self.name_size = name_size
        self.namespace_name = namespace_name

    @classmethod
    def get_fields(cls) -> Dict:
        return {
            1: ('duration', p.UVarintType, 0),
            2: ('parent_id', p.UVarintType, 0),
            3: ('id', p.UVarintType, 0),
            4: ('registration_type', p.EnumType("NEM2NamespaceRegistrationType", (0, 1)), 0),  # default=ROOT
            5: ('name_size', p.UVarintType, 0),
            6: ('namespace_name', p.BytesType, 0),
        }
