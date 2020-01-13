from micropython import const

from apps.common import HARDENED

NEM2_NETWORK_MAIN_NET = const(0x68)
NEM2_NETWORK_TEST_NET = const(0x98)
NEM2_NETWORK_MIJIN = const(0x60)
NEM2_NETWORK_MIJIN_TEST = const(0x90)

NEM2_TRANSACTION_TYPE_TRANSFER = const(0x4154)
NEM2_TRANSACTION_TYPE_MOSAIC_DEFINITION = const(0x414D)
NEM2_TRANSACTION_TYPE_MOSAIC_SUPPLY = const(0x424D)
NEM2_TRANSACTION_TYPE_AGGREGATE_BONDED = const(0x4241)
NEM2_TRANSACTION_TYPE_AGGREGATE_COMPLETE = const(0x4141)
NEM2_TRANSACTION_TYPE_NAMESPACE_REGISTRATION = const(0x414E)
NEM2_TRANSACTION_TYPE_ADDRESS_ALIAS = const(0x424E)
NEM2_TRANSACTION_TYPE_NAMESPACE_METADATA = const(0x4344)
NEM2_TRANSACTION_TYPE_MOSAIC_METADATA = const(0x4244)
NEM2_TRANSACTION_TYPE_ACCOUNT_METADATA = const(0x4144)
NEM2_TRANSACTION_TYPE_MOSAIC_ALIAS = const(0x434E)
NEM2_TRANSACTION_TYPE_HASH_LOCK = const(0x4148)
NEM2_TRANSACTION_TYPE_SECRET_LOCK = const(0x4152)
NEM2_TRANSACTION_TYPE_SECRET_PROOF = const(0x4252)
NEM2_TRANSACTION_TYPE_MULTISIG_MODIFICATION = const(0x4155)
NEM2_TRANSACTION_TYPE_ACCOUNT_ADDRESS_RESTRICTION = const(0x4150)
NEM2_TRANSACTION_TYPE_ACCOUNT_MOSAIC_RESTRICTION = const(0x4250)
NEM2_TRANSACTION_TYPE_ACCOUNT_OPERATION_RESTRICTION = const(0x4350)
NEM2_TRANSACTION_TYPE_ACCOUNT_LINK = const(0x414C)

NEM2_NAMESPACE_REGISTRATION_TYPE_ROOT = const(0x00)
NEM2_NAMESPACE_REGISTRATION_TYPE_SUB = const(0x01)

NEM2_ALIAS_ACTION_TYPE_LINK = const(0x01)
NEM2_ALIAS_ACTION_TYPE_UNLINK = const(0x00)

NEM2_MOSAIC_SUPPLY_CHANGE_ACTION_INCREASE = const(0x01)
NEM2_MOSAIC_SUPPLY_CHANGE_ACTION_DECREASE = const(0x00)

NEM2_SECRET_LOCK_SHA3_256 = const(0x00)
NEM2_SECRET_LOCK_KECCAK_256 = const(0x01)
NEM2_SECRET_LOCK_HASH_160 = const(0x02)
NEM2_SECRET_LOCK_HASH_256 = const(0x03)

NEM2_ACCOUNT_RESTRICTION_ALLOW_INCOMING_ADDRESS = const(0x01)
NEM2_ACCOUNT_RESTRICTION_ALLOW_MOSAIC = const(0x02)
NEM2_ACCOUNT_RESTRICTION_ALLOW_INCOMING_TRANSACTION_TYPE = const(0x04)
NEM2_ACCOUNT_RESTRICTION_ALLOW_OUTGOING_ADDRESS = const(0x4001)
NEM2_ACCOUNT_RESTRICTION_ALLOW_OUTGOING_TRANSACTION_TYPE = const(0x4004)
NEM2_ACCOUNT_RESTRICTION_BLOCK_INCOMING_ADDRESS = const(0x8001)
NEM2_ACCOUNT_RESTRICTION_BLOCK_MOSAIC = const(0x8002)
NEM2_ACCOUNT_RESTRICTION_BLOCK_INCOMING_TRANSACTION_TYPE = const(0x8004)
NEM2_ACCOUNT_RESTRICTION_BLOCK_OUTGOING_ADDRESS = const(0xC001)
NEM2_ACCOUNT_RESTRICTION_BLOCK_OUTGOING_TRANSACTION_TYPE = const(0xC004)

NEM2_MAX_DIVISIBILITY = const(6)
NEM2_MAX_SUPPLY = const(9000000000000000)
NEM2_MOSAIC_AMOUNT_DIVISOR = const(1000000)

NEM2_SALT_SIZE = const(32)
AES_BLOCK_SIZE = const(16)
NEM2_HASH_ALG = "keccak"
NEM2_PUBLIC_KEY_SIZE = const(32)  # ed25519 public key

NEM2_MAX_PLAIN_PAYLOAD_SIZE = const(1024)
NEM2_MAX_ENCRYPTED_PAYLOAD_SIZE = const(960)

# Should be the key that maps to the transaction data
map_type_to_friendly_name = {
    NEM2_TRANSACTION_TYPE_TRANSFER: "ransfer",
    NEM2_TRANSACTION_TYPE_MOSAIC_DEFINITION: "mosaic definition",
    NEM2_TRANSACTION_TYPE_MOSAIC_SUPPLY: "mosaic supply",
    NEM2_TRANSACTION_TYPE_NAMESPACE_REGISTRATION: "namespace registration",
    NEM2_TRANSACTION_TYPE_ADDRESS_ALIAS: "address alias",
    NEM2_TRANSACTION_TYPE_MOSAIC_ALIAS: "mosaic alias",
    NEM2_TRANSACTION_TYPE_NAMESPACE_METADATA: "namespace metadata",
    NEM2_TRANSACTION_TYPE_MOSAIC_METADATA: "mosaic metadata",
    NEM2_TRANSACTION_TYPE_ACCOUNT_METADATA: "account metadata",
    NEM2_TRANSACTION_TYPE_HASH_LOCK: "hash lock",
    NEM2_TRANSACTION_TYPE_SECRET_LOCK: "secret lock",
    NEM2_TRANSACTION_TYPE_SECRET_PROOF: "secret proof"
}

def validate_nem2_path(path: list) -> bool:
    """
    Validates derivation path to fit 44'/43'/a'/0'/0',
    where `a` is an account number.
    """
    length = len(path)
    if length != 5:
        return False
    if path[0] != 44 | HARDENED:
        return False
    if not (
        path[1] == 43 | HARDENED
    ):
        return False
    if path[2] < HARDENED or path[2] > 1000000 | HARDENED:
        return False
    if (path[3] != 0 | HARDENED or path[4] != 0 | HARDENED):
        return False
    return True


def captialize_string(s):
    s = list(s)
    s[0] = s[0].upper()
    return "".join(s)

# the smallest protobuf integer size is 32 bits
# nem2 catapult uses a signed 8 bit integer for minApprovalDelta and minRemovalDelta
# this function is used to convert between the signed 8 bit integers sent by the sdk
# to the uint32 data type as defined in the protobuf message
def unsigned_32_bit_int_to_8_bit(unsigned_32_bit_int, signed=False):
    unsigned_8_bit_int = unsigned_32_bit_int & 0x000000ff
    if(signed and unsigned_8_bit_int > 127):
        return unsigned_8_bit_int - 256
    return unsigned_8_bit_int