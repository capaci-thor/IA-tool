from scipy.spatial import distance
import pandas as pd


def minkowski(path, x):
    data = pd.read_csv(path)
    Lista = []
    for i in range(0, len(data)):
        Lista.append([int(data.values[i,j]) 
        for j in range(1, len(data.columns))])

    distancias_minkowski=[]

    for i in range(0,len(data)):
        a = []
        for j in range(0,len(data)):
            a.append(distance.minkowski(Lista[i], Lista[j], x))
        distancias_minkowski.append(a)
    df_minkowski = pd.DataFrame(distancias_minkowski)
    
    return df_minkowski, distancias_minkowski
