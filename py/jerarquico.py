from os import path
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import seaborn as sns
import scipy.cluster.hierarchy as shc 
from sklearn.cluster import AgglomerativeClustering
import matplotlib.pyplot as plt
import pickle
import tkinter as tk


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



def jerarquico(path):
    data = pd.read_csv(path)
    correlacion = data.corr("pearson")

    MatrizVariables = delcorrelation(correlacion, 0.78)
    lista = list(MatrizVariables.columns)
    #print(lista)
    matriz = []

    matriz = np.array(data[[i for i in lista ]])
    pd.DataFrame(matriz)

    plt.figure(figsize=(10,7))
    plt.title("pacientes con cancer de mama")
    plt.xlabel("Observaciones")
    plt.ylabel("Distancias")
    Arbol = shc.dendrogram(shc.linkage(matriz, method="complete", metric="euclidean"))
    plt.show()
    MJerarquico = AgglomerativeClustering(n_clusters = 5, linkage= "complete", affinity = "euclidean")
    MJerarquico.fit_predict(matriz)
    data["clusterH"] =  MJerarquico.labels_
    bx(str(data.groupby(["clusterH"])["clusterH"].count()))

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

    #print(colname)

    return dataset

jerarquico(path)