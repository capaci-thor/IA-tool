from scipy.spatial import distance
import pandas as pd


def manhattan(path):
    data = pd.read_csv(path)
    Lista = []
    for i in range(0,  len(data)):
        Lista.append([int(data.values[i,j]) 
        for j in range(1, len(data.columns))])

    distancias_manhattan = []

    for i in range(0,len(data)):
        a = []
        for j in range(0, len(data)):
            a.append(distance.cityblock(Lista[i], Lista[j]))
        distancias_manhattan.append(a)
    df_manhattan = pd.DataFrame(distancias_manhattan)
    
    return df_manhattan, distancias_manhattan
