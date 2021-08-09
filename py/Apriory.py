import numpy as np        #Para trabajar con vectores y matrices de n dimensiones
import pandas as pd

from apyori import apriori


def Apriory(path):
    data = pd.read_csv(path)
    print("1")
    Lista = []
    for i in range(0, 750):#7500
        Lista.append([str(data.values[i,j]) for j in range(0,20)])
        #print(i)

    print("Aqui vamos")

    Reglas = apriori(Lista, min_support = 0.0045, min_confidence = 0.2, min_lift = 3, min_length = 2)
    Resultados = list(Reglas)
    return Resultados, True