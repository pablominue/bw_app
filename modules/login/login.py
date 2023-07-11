from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivymd.app import MDApp

from .validation import validate_credentials

class LoginWin(Widget):
    lg_username = ObjectProperty(None)
    lg_password = ObjectProperty(None)
    app = MDApp.get_running_app()
    def on_press(self):
        valid = validate_credentials(self.lg_username.text,
                                     self.lg_password.text)
        if valid:
            self.app.root.current = 'screen_app'
        else:
            #self.app.root.current_screen.parent.current = 'wrong_credentials'
            self.app.root.current = 'wrong_credentials'

        
    
    def signin(self):
        self.app.root.current = 'signin_app'

