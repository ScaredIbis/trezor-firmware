from trezor.messages.NEM2TransactionCommon import NEM2TransactionCommon

from apps.common.writers import write_bytes, write_uint32_le, write_uint64_le


def serialize_tx_common(
    common: NEM2TransactionCommon,
    public_key: bytearray
) -> bytearray:
    w = bytearray()

    write_uint32_le(w, common.type)
    write_uint32_le(w, common.network_type)
    write_uint32_le(w, common.version)    
    write_uint64_le(w, common.max_fee)
    write_bytes_with_len(w, common.deadline)
    write_bytes_with_len(w, public_key)

    return w


def write_bytes_with_len(w, buf: bytes):
    write_uint32_le(w, len(buf))
    write_bytes(w, buf)
