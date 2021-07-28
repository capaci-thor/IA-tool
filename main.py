import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang.builder import Builder


kivy.require("1.9.2")
Builder.load_file('Main.kv')

class RelativeLL(BoxLayout):
    pass

class MyApp(App):
    title = "IA Tool"
    Window.maximize()

    def build(self):       
        return RelativeLL()
        

if __name__ == "__main__":
    MyApp().run()



