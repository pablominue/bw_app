import kivy
kivy.require('2.2.1')

import os

from kivy.lang import Builder
from kivymd.app import MDApp

class MainApp(MDApp):
    def build(self):
        return Builder.load_file('main.kv')
 
if __name__ == '__main__':
    for root, dirs, files in os.walk('widgets'):
        for file in files:
            if file.endswith('.kv'):
                Builder.load_file(os.path.join(root, file))
    MainApp().run()