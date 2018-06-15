# Automatically generated by pb2py
import protobuf as p


class Ping(p.MessageType):
    MESSAGE_WIRE_TYPE = 1
    FIELDS = {
        1: ('message', p.UnicodeType, 0),
        2: ('button_protection', p.BoolType, 0),
        3: ('pin_protection', p.BoolType, 0),
        4: ('passphrase_protection', p.BoolType, 0),
    }

    def __init__(
        self,
        message: str = None,
        button_protection: bool = None,
        pin_protection: bool = None,
        passphrase_protection: bool = None
    ) -> None:
        self.message = message
        self.button_protection = button_protection
        self.pin_protection = pin_protection
        self.passphrase_protection = passphrase_protection