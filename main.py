from enum import Flag
from sys import flags
import kivy
from kivy import app
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget



kivy.require("1.9.2")
Builder.load_file('Main.kv')

class RelativeLL(BoxLayout):

    def __init__(self):
        super(RelativeLL, self).__init__()
        self.BtnMe = BtnMetrics()
        self.BtnC = BtnClu()
        self.flag = False

    #Metodo onClick del boton metricas de similitud
    def menuMetrics(self):
        if(self.flag == False):
            self.flag = True
            self.add_widget(self.BtnMe)
            self.remove_widget(self.BtnC)
        elif(self.flag == True):
            self.flag = False
            self.remove_widget(self.BtnMe)

    #Metodo onClick del boton clustering        
    def menuClustering(self):
        if(self.flag == False):
            self.flag = True
            self.add_widget(self.BtnC)
            self.remove_widget(self.BtnMe)
        elif(self.flag == True):
            self.flag = False
            self.remove_widget(self.BtnC)

    #Metodos para los botones de las diferentes metricas.
    def Euclidean(self):
        self.flag = False
        self.remove_widget(self.BtnMe)

    def Chebyshev(self):
        self.flag = False
        self.remove_widget(self.BtnMe)

    def Manhattan(self):
        self.flag = False
        self.remove_widget(self.BtnMe)

    def Minkowsky(self):
        self.flag = False
        self.remove_widget(self.BtnMe)

    #Metodos para los botones de clustering
    def jer(self):
        self.flag = False
        self.remove_widget(self.BtnC)

    def kmeans(self):
        self.flag = False
        self.remove_widget(self.BtnC)


class BtnMetrics(BoxLayout):
    None

class BtnClu(BoxLayout):
    None

class MyApp(App):
    title = "IA Tool"
    Window.maximize()

    def build(self):       
        return RelativeLL()
        

if __name__ == "__main__":
    app = MyApp()
    app.run()



