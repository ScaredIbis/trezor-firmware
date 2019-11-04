from .nem2_mosaics import mosaics


def get_mosaic_definition(mosaic_id: int, network: int) -> dict:
    for m in mosaics:
        if mosaic_id == m["id"]:
            if ("networks" not in m) or (network in m["networks"]):
                return m
    return None


def is_nem_xem_mosaic(mosaic_id: str) -> bool:
    if mosaic_id == int("85BBEA6CC462B244", 16):
        return True
    return False