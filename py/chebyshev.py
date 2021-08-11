from scipy.spatial import distance
import pandas as pd


def chebyshev(path):
    data = pd.read_csv(path)
    Lista = []
    for i in range(0, len(data)):
        Lista.append([int(data.values[i,j]) 
        for j in range(1, len(data.columns))])

    distancias_chebyshev=[]

    for i in range(0,len(data)):
        a = []
        for j in range(0, len(data)):
            a.append(distance.chebyshev(Lista[i], Lista[j]))
        distancias_chebyshev.append(a)
    df_chebyshev = pd.DataFrame(distancias_chebyshev)
    
    return df_chebyshev, distancias_chebyshev
