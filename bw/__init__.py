from bw.Biwenger.biwenger import (
    Pack, Player, Team, Data
)

data = Data()

def get_pack(type: str) -> str:
    pack = Pack(type_=type,
                data = data.data)
    return pack.profit_chance()

