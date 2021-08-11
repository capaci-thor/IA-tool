import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.cluster import KMeans 
# Bibliotecas para clustering k-means
from sklearn.metrics import pairwise_distances_argmin_min
from kneed import KneeLocator
import tkinter as tk
import pickle




with open("py\obj.pickle", "rb") as f:
    path = pickle.load(f)




def bx(text):
    root = tk.Tk()


    canvas = tk.Canvas(root)
    canvas.pack(side=tk.LEFT)

    scrollbar = tk.Scrollbar(root, command=canvas.yview)
    scrollbar.pack(side=tk.LEFT, fill='y')

    canvas.configure(yscrollcommand = scrollbar.set)

    frame = tk.Frame(canvas)
    canvas.create_window((0,0), window=frame, anchor='nw')

    tk.Label(frame, text=text).pack()


    root.mainloop()


def kmeans(path):

    data = pd.read_csv(path)
    correlacion = data.corr("pearson")

    MatrizVariables = delcorrelation(correlacion, 0.78)
    lista = list(MatrizVariables.columns)
    #print(lista)
    matriz = []

    matriz = np.array(data[[i for i in lista ]])
    pd.DataFrame(matriz)

    SSE =[]
    for i in range(2,11):
        km = KMeans(n_clusters=i, random_state=0)
        km.fit(matriz)
        SSE.append(km.inertia_)

    kl = KneeLocator(range(2,11), SSE, curve = "convex", direction = "decreasing")

    MParticional = KMeans(n_clusters=kl.elbow , random_state=0).fit(matriz)
    MParticional.predict(matriz)
    data["clusterP"] = MParticional.labels_
    bx(str(data.groupby(["clusterP"])["clusterP"].count()))

    plt.figure(figsize=(10,7))
    plt.scatter(matriz[:,0], matriz[:,1], c=MParticional.labels_ , cmap="rainbow")
    plt.show()




def delcorrelation(dataset, threshold):
    col_corr = set() # Set of all the names of deleted columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if (corr_matrix.iloc[i, j] >= threshold) and (corr_matrix.columns[j] not in col_corr):
                colname = corr_matrix.columns[i] # getting the name of column
                col_corr.add(colname)
                if colname in dataset.columns:
                    del dataset[colname] # deleting the column from the dataset

    return dataset



kmeans(path)
