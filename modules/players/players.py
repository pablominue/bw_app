from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown
from kivymd.app import MDApp
from kivy.factory import Factory
import os
import bw

class PlayerWin(Widget):
    playersearch = ObjectProperty(None)
    def search_player(self, player):
        profit = bw.get_player_profit(
            player
        )
        profit_value = profit
        if profit.__contains__('Found'):
            self.parent.parent.player = str(profit)
            self.parent.parent.player_img_path = 'assets/images/error.png'
            self.parent.parent.current = 'playerresult'
            return
        else:
            profit += " profitability"

        self.parent.parent.player = str(profit)
        if float(profit_value) >= 0.50:
            self.parent.parent.player_img_path = 'assets/images/good_prof.png'
        else:
            self.parent.parent.player_img_path = 'assets/images/bad_prof.png'

        self.parent.parent.current = 'playerresult'

class PlayerResult(Widget):
    pass
