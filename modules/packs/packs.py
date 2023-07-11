from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.dropdown import DropDown
from kivymd.app import MDApp
from kivy.factory import Factory
import os
import bw
global PACK
PACK = ''

class PackWin(Widget):
    #pack_selection = ObjectProperty(None)
    selection = ''
    app = MDApp.get_running_app()
    def button_press(self, _type):
        self.selection = _type
        PACK = _type
        print(PACK) 
        self.parent.parent.current = 'packresult'
        #self.root.sm_sub.current='packresult'

class PackResult(Widget):
    app = MDApp.get_running_app()
    selectionpack = PACK
    def selection_pack(self, value: str):
        self.ids.selection.text = value
        print(
            bw.get_pack(
            PACK)
        )    

class SelectPack(Widget):
    pack_selection = ObjectProperty(None)
    app = MDApp.get_running_app()
    def selection_pack(self, value: str):
        self.pack_selection = value
        print(self.pack_selection)