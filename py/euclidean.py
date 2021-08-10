import tkinter
from scipy.spatial import distance
import pandas as pd


def euclidean(path):
    data = pd.read_csv(path)
    #print(data)
    Lista = []
    for i in range(0, 15):
        Lista.append([int(data.values[i,j]) 
        for j in range(1, 9)])

    distancias_euclideana=[]

    for i in range(0,14):
        a = []
        for j in range(0,14):
            a.append(distance.euclidean(Lista[i], Lista[j]))
        distancias_euclideana.append(a)
    df_euclideano = pd.DataFrame(distancias_euclideana)

    return df_euclideano, distancias_euclideana
