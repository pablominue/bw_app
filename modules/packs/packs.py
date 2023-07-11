from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown
from kivymd.app import MDApp
from kivy.factory import Factory
import os
import bw

class PackWin(Widget):
    app = MDApp.get_running_app()
    def button_press(self, _type):
        chance = bw.get_pack(
            _type
        )
        chance += " of profit"
        self.parent.parent.pack = str(chance)
        self.parent.parent.current = 'packresult'

class PackResult(Widget):
    pass

# class PackResult(Widget):
#     app = MDApp.get_running_app()
#     def selection_pack(self, value: str):
#         result = bw.get_pack(
#             self.parent.parent.pack
#         )
#         return result
