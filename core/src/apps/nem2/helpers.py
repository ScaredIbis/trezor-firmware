from micropython import const

from apps.common import HARDENED

NEM2_NETWORK_MAIN_NET = const(0x68)
NEM2_NETWORK_TEST_NET = const(0x98)
NEM2_NETWORK_MIJIN = const(0x60)
NEM2_NETWORK_MIJIN_TEST = const(0x90)

NEM2_TRANSACTION_TYPE_TRANSFER = const(0x4154)
NEM2_TRANSACTION_TYPE_MOSAIC_DEFINITION = const(0x414D)
NEM2_TRANSACTION_TYPE_AGGREGATE_BONDED = const(0x4241)
NEM2_TRANSACTION_TYPE_AGGREGATE_COMPLETE = const(0x4141)
NEM2_TRANSACTION_TYPE_NAMESPACE_REGISTRATION = const(0x414E)
NEM2_TRANSACTION_TYPE_ADDRESS_ALIAS = const(0x424E)
NEM2_TRANSACTION_TYPE_MOSAIC_ALIAS = const(0x434E)

NEM2_NAMESPACE_REGISTRATION_TYPE_ROOT = const(0x00)
NEM2_NAMESPACE_REGISTRATION_TYPE_SUB = const(0x01)

NEM2_ALIAS_ACTION_TYPE_LINK = const(0x01)
NEM2_ALIAS_ACTION_TYPE_UNLINK = const(0x00)

NEM2_MAX_DIVISIBILITY = const(6)
NEM2_MAX_SUPPLY = const(9000000000000000)
NEM2_MOSAIC_AMOUNT_DIVISOR = const(1000000)

NEM2_SALT_SIZE = const(32)
AES_BLOCK_SIZE = const(16)
NEM2_HASH_ALG = "keccak"
NEM2_PUBLIC_KEY_SIZE = const(32)  # ed25519 public key

NEM2_MAX_PLAIN_PAYLOAD_SIZE = const(1024)
NEM2_MAX_ENCRYPTED_PAYLOAD_SIZE = const(960)

def check_path(path: list) -> bool:
    """
    Validates derivation path to fit 44'/43'/a'
    """
    length = len(path)
    if length != 3:
        return False
    if path[0] != 44 | HARDENED:
        return False
    if path[1] != 43 | HARDENED:
        return False
    if path[2] < HARDENED or path[2] > 1000000 | HARDENED:
        return False
    return True

def captialize_string(s):
    s = list(s)
    s[0] = s[0].upper()
    return "".join(s)
