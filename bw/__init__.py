from bw.Biwenger.biwenger import (
    Pack, Player, Team, Data
)
import pandas as pd

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
    
def export_data(path: str, filename: str, format_: str = 'csv') -> bool:
    if filename.__contains__('.') == False:
        filename += f".{format_}"
    if path.__contains__(f'.'):
        format_ = path.split(
            '.'
        )[1]
    else:
        path += filename
        path += format_
    try:
        getattr(
            data.data,
            f"to_{format_}"
        )(
            path
        )
        return True
    except:
        return False
