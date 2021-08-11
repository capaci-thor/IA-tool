import tkinter
from scipy.spatial import distance
import pandas as pd

def euclidean(path):
    data = pd.read_csv(path)
    Lista = []
    for i in range(0, len(data)):
        Lista.append([int(data.values[i,j]) 
        for j in range(1, len(data.columns))])
    
    distancias_euclideana=[]

    for i in range(0, len(data)):
        a = []
        for j in range(0, len(data)):
            a.append(distance.euclidean(Lista[i], Lista[j]))
        distancias_euclideana.append(a)
    df_euclideano = pd.DataFrame(distancias_euclideana)

    return df_euclideano, distancias_euclideana
