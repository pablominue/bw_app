from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button, ButtonBehavior
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivymd.app import MDApp


class SigninWin(Widget):
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    app = MDApp.get_running_app()
    

    def on_press(self):
        self.text_inputs = {
            'name': self.username,
            'email': self.email,
            'password': self.password
        }
        valid = True
        for k, v in self.text_inputs.items():
            if len(v.text) == 0:
                print(f"All text fields must be filled: {k}!")
                valid=False
        if valid:
            self.app.root.current = 'screen_app'

 

# class Form(GridLayout):
#     def __init__(self, **kwargs):
#         super(Form, self).__init__(**kwargs)
        
#         self.cols = 1
        
#         self.add_widget(Label(text = 'Enter User Name'))
#         self.username = TextInput(multiline=False)
#         self.add_widget(self.username)

#         self.add_widget(Label(text = 'Enter email'))
#         self.email = TextInput(multiline=False)
#         self.add_widget(self.email)

#         self.add_widget(Label(text = 'Enter Password'))
#         self.password = TextInput(password=True, multiline=False)
#         self.add_widget(self.password)

#         self.add_widget(Label(text = 'Repeat Password'))
#         self.password_check = TextInput(password=True, multiline=False)
#         self.add_widget(self.password_check)

#         self.text_inputs = {
#             'user': self.username,
#             'mail': self.email, 
#             'password': self.password,
#             'password_check': self.password_check
#         }


# class SigninWin(GridLayout):
#     def __init__(self, **kwargs):
#         super(SigninWin, self).__init__(**kwargs)
#         self.cols = 1
#         self.form = Form()
#         self.add_widget(self.form)
#         self.sumbit_button = Button(
#             text = 'Sign In',
#             font_size = 40
#         )
#         self.sumbit_button.bind(on_press=self.on_press)
#         self.add_widget(self.sumbit_button)
        
#     def on_press(self, instance):
#         if self.form.password != self.form.password_check:
#             print('Passwords must be the same')
        
#         for k, v in self.form.text_inputs.items():
#             if len(v.text) == 0:
#                 print(f"All text fields must be filled: {k}!")
#         print('pressed')