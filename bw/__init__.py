from bw.Biwenger.biwenger import (
    Pack, Player, Team, Data
)

data = Data()

def get_pack(type: str) -> str:
    pack = Pack(type_=type,
                data = data.data)
    return pack.profit_chance()

def get_player_profit(player: str) -> str:
    try:
        print(player)
        player_ = Player(data= data,
                        name = player)
        prof = str(player_.profitability)
        prof = prof[0:6]
        return prof
    except Exception as e:
        print(e)
        return "Player not Found"
    