from scipy.spatial import distance
import pandas as pd


def minkowski(path):
    data = pd.read_csv(path)
    print(data)
    Lista = []
    for i in range(0, 15):
        Lista.append([int(data.values[i,j]) 
        for j in range(1, 9)])

    distancias_minkowski=[]

    for i in range(0,14):
        a = []
        for j in range(0,14):
            a.append(distance.minkowski(Lista[i], Lista[j],1.5))
        distancias_minkowski.append(a)
    df_minkowski = pd.DataFrame(distancias_minkowski)
    
    return df_minkowski, distancias_minkowski
