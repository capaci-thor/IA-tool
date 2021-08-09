from tkinter.constants import END
import kivy
from kivy import app
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput

#from tkinter import *
import tkinter as tk
from tkinter import filedialog
from py import Apriory
import pandas as pd       # Para la manipulación de análisis de datos

import pickle
from os import system

kivy.require("1.9.2")
Builder.load_file('kv\Main.kv')
Builder.load_file('kv\Apriory.kv')
Builder.load_file('kv\euclidean.kv')
Builder.load_file('kv\chebyshev.kv')
Builder.load_file('kv\minkowski.kv')
Builder.load_file('kv\manhattan.kv')


def Datos(path):
    datos = pd.read_csv(path)
    

class RelativeLL(BoxLayout):

    def __init__(self):
        super(RelativeLL, self).__init__()
        self.BtnMe = BtnMetrics()
        self.BtnC = BtnClu()
        self.flag = False #bandera para mostroar u ocultar menu
        #BoxLayout algoritmo apriory
        self.BLApriory = AprioryBox()
        #BoxLayout algoritmos metricas
        self.BLEuclidean = EuclideanBox()
        self.BLChebyshev = ChebyshevBox()
        self.BLMinkowski = MinkowskiBox()
        self.BLManhattan = ManhattanBox()
        self.direccion = ""
    


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
        try:
            self.ids.blApriory.remove_widget(self.BLApriory)
            self.ids.blApriory.remove_widget(self.BLEuclidean)
            self.ids.blApriory.remove_widget(self.BLChebyshev)
            self.ids.blApriory.remove_widget(self.BLManhattan)
            self.ids.blApriory.remove_widget(self.BLMinkowski)
        except:
            None
        self.ids.blApriory.add_widget(self.BLEuclidean)

    def Chebyshev(self):
        self.flag = False
        self.remove_widget(self.BtnMe)
        try:
            self.ids.blApriory.remove_widget(self.BLApriory)
            self.ids.blApriory.remove_widget(self.BLEuclidean)
            self.ids.blApriory.remove_widget(self.BLChebyshev)
            self.ids.blApriory.remove_widget(self.BLManhattan)
            self.ids.blApriory.remove_widget(self.BLMinkowski)
        except:
            None
        self.ids.blApriory.add_widget(self.BLChebyshev)


    def Manhattan(self):
        self.flag = False
        self.remove_widget(self.BtnMe)
        try:
            self.ids.blApriory.remove_widget(self.BLApriory)
            self.ids.blApriory.remove_widget(self.BLEuclidean)
            self.ids.blApriory.remove_widget(self.BLChebyshev)
            self.ids.blApriory.remove_widget(self.BLManhattan)
            self.ids.blApriory.remove_widget(self.BLMinkowski)
        except:
            None
        self.ids.blApriory.add_widget(self.BLManhattan)


    def Minkowsky(self):
        self.flag = False
        self.remove_widget(self.BtnMe)
        try:
            self.ids.blApriory.remove_widget(self.BLApriory)
            self.ids.blApriory.remove_widget(self.BLEuclidean)
            self.ids.blApriory.remove_widget(self.BLChebyshev)
            self.ids.blApriory.remove_widget(self.BLManhattan)
            self.ids.blApriory.remove_widget(self.BLMinkowski)
        except:
            None
        self.ids.blApriory.add_widget(self.BLMinkowski)

    def aplicarEuclidean(self):
        from py import euclidean

        eu , lista = euclidean.euclidean(self.direccion)
        #print(eu)
        #print(lista)
        with open("py/obj.pickle", "wb") as f:
            pickle.dump(lista, f)
        system("python py/showList.py")


    def aplicarChebyshev(self):
        from py import chebyshev

        ch , lista = chebyshev.chebyshev(self.direccion)

        with open("py/obj.pickle", "wb") as f:
            pickle.dump(lista, f)
        system("python py/showList.py")

    def aplicarManhattan(self):
        from py import manhattan

        man, lista = manhattan.manhattan(self.direccion)
        with open("py/obj.pickle", "wb") as f:
            pickle.dump(lista, f)
        system("python py/showList.py")

    def aplicarMinkowski(self):
        from py import minkowsk

        eu, lista = minkowsk.minkowski(self.direccion)
        with open("py/obj.pickle", "wb") as f:
            pickle.dump(lista, f)
        system("python py/showList.py")

    #Metodos para los botones de clustering
    def jer(self):
        self.flag = False
        self.remove_widget(self.BtnC)

    def kmeans(self):
        self.flag = False
        try:
            self.remove_widget(self.BtnC)
        except:
            None


    #Metodo para cargar archivo
    def cargar(self):
        root = tk.Tk()
        root.withdraw()
        self.direccion =filedialog.askopenfilename(title = "Select file",filetypes = (("CSV Files","*.csv"),))
        if(self.direccion != ""):
            Datos(self.direccion)
            self.BLApriory.cargaTexto = "Archivo cargado"
            self.BLEuclidean.cargaTexto = "Archivo cargado"
            self.BLMinkowski.cargaTexto = "Archivo cargado"
            self.BLChebyshev.cargaTexto = "Archivo cargado"
            self.BLManhattan.cargaTexto = "Archivo cargado"

        else:
            self.BLApriory.cargaTexto = "no se cargó ningun archivo"
            self.BLEuclidean.cargaTexto = "no se cargó ningun archivo"
            self.BLMinkowski.cargaTexto = "no se cargó ningun archivo"
            self.BLChebyshev.cargaTexto = "no se cargó ningun archivo"
            self.BLManhattan.cargaTexto = "no se cargó ningun archivo"




        ### Algoritmo apriory
    
    def apriori(self):
        #elimina si ya hay una existente
        try:
            self.ids.blApriory.remove_widget(self.BLApriory)
            self.ids.blApriory.remove_widget(self.BLEuclidean)
            self.ids.blApriory.remove_widget(self.BLChebyshev)
            self.ids.blApriory.remove_widget(self.BLManhattan)
            self.ids.blApriory.remove_widget(self.BLMinkowski)
        except:
            None
        self.ids.blApriory.add_widget(self.BLApriory)

    def aplicarApriory(self):
        bandera = False

        from py import Apriory
        lista, bandera = Apriory.Apriory(self.direccion)
        for item in lista:
            Emparejar = item[0]
            items = [x for x in Emparejar]
            print("Regla: " + str(item[0]))



        if(bandera):
            print("Listo")
        else:
            print("cargando")


class BtnMetrics(BoxLayout):
    None

class BtnClu(BoxLayout):
    None

class AprioryBox(BoxLayout):
    cargaTexto = StringProperty()

    def __init__(self):
        super().__init__()
        self.cargaTexto = ""




class EuclideanBox(BoxLayout):
    cargaTexto = StringProperty()
    Lista = StringProperty()
    def __init__(self):
        super().__init__()
        self.cargaTexto = ""
        self.Lista = ""

class ChebyshevBox(BoxLayout):
    cargaTexto = StringProperty()

    def __init__(self):
        super().__init__()
        self.cargaTexto = ""


class MinkowskiBox(BoxLayout):
    cargaTexto = StringProperty()

    def __init__(self):
        super().__init__()
        self.cargaTexto = ""


class ManhattanBox(BoxLayout):
    cargaTexto = StringProperty()

    def __init__(self):
        super().__init__()
        self.cargaTexto = ""

 
    
class MyApp(App):
    title = "IA Tool"
    Window.maximize()

    def build(self):       
        return RelativeLL()
        

if __name__ == "__main__":
    app = MyApp()
    app.run()



