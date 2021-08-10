from logging import root
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

from numpy import string_
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
        self.support = ""
        self.confidence = ""
        self.lift = ""
        self.len = ""
        self.BLApriory = AprioryBox()
        #BoxLayout algoritmos metricas
        self.BLEuclidean = EuclideanBox()
        self.BLChebyshev = ChebyshevBox()
        self.BLMinkowski = MinkowskiBox()
        self.minko = ""
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
        try:
            from py import minkowsk

            eu, lista = minkowsk.minkowski(self.direccion, self.minko)
            with open("py/obj.pickle", "wb") as f:
                pickle.dump(lista, f)
            system("python py/showList.py")
        except:
            self.BLMinkowski.minko = "ingrese un numero valido"

    def processMi(self):
        minko = self.BLMinkowski.ids.TIMinko.text
        try:
            self.minko = float(minko)
            self.BLMinkowski.minko = "OK"
        except:
            self.BLMinkowski.minko = "Formato no valio"


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
        self.BLApriory.cargando = "Falló"
        f = open ('py\Apriory_datos.txt','w')
        try:
            bandera = False
            from py import Apriory
            
            lista, bandera = Apriory.Apriory(self.direccion, self.support, self.confidence, self.lift, self.len)
            for item in lista:
                Emparejar = item[0]
                items = [x for x in Emparejar]
                #print(informacion)
                f.write( "regla: " + str(item[0]))
                f.write( "\nsoporte" +str(item[1]))
                f.write( "\nConfianza: " + str(item[2][0][2]))
                f.write( "\nElevación: " + str(item[2][0][3]) + "\n")
                f.write("______________________________________________\n")
                #print("Regla: " + str(item[0]))

            f.close()

            if(bandera):
                self.BLApriory.cargando = "Listo"

            else:
                self.BLApriory.cargando = "Falló"

        except:
            self.BLApriory.cargando = "No hay información o no es compatible"

    def ShowApriory(self):
        system("python py\Aprirori_show.py")

    def process(self):
        support = self.BLApriory.ids.support.text
        confidence = self.BLApriory.ids.confidence.text
        lift = self.BLApriory.ids.lift.text
        len = self.BLApriory.ids.len.text

        try:
            self.support = float(support)
            self.BLApriory.support = "OK"
        except:
            self.BLApriory.support = "Formato no valio"
        try:
            self.confidence = float(confidence)
            self.BLApriory.confidence = "OK"
        except:
            self.BLApriory.confidence = "Formato no valio"
        try:
            self.lift = float(lift)
            self.BLApriory.lift = "OK"
        except:
            self.BLApriory.lift = "Formato no valio"

        try:
            self.len = int(len)
            self.BLApriory.length = "OK"
        except:
            self.BLApriory.length = "Formato no valio"
        




class BtnMetrics(BoxLayout):
    None

class BtnClu(BoxLayout):
    None

class AprioryBox(BoxLayout):
    cargaTexto = StringProperty()
    cargando = StringProperty()
    support = StringProperty()
    confidence = StringProperty()
    lift = StringProperty()
    length = StringProperty()
    
    def __init__(self):
        super().__init__()
        self.cargaTexto = ""
        self.cargando = ""
        self.support = ""
        self.confidence = ""
        self.lift = ""
        self.length = ""
       




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
    minko = StringProperty()

    def __init__(self):
        super().__init__()
        self.cargaTexto = ""
        self.minko = ""


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
