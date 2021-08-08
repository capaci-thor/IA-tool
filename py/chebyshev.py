from scipy.spatial import distance
import pandas as pd


def chebyshev(path):
    data = pd.read_csv(path)
    print(data)
    Lista = []
    for i in range(1, 15):
        Lista.append([int(data.values[i,j]) 
        for j in range(1, 9)])

    distancias_chebyshev=[]

    for i in range(0,14):
        a = []
        for j in range(0,14):
            a.append(distance.chebyshev(Lista[i], Lista[j]))
        distancias_chebyshev.append(a)
    df_chebyshev = pd.DataFrame(distancias_chebyshev)
    
    return df_chebyshev
