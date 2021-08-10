#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
import numpy as np        #Para trabajar con vectores y matrices de n dimensiones
import pandas as pd

from apyori import apriori


def Apriory(path, support, confidence, lift, length):
    data = pd.read_csv(path)

    Lista = []
    #print(len(data))
    #print(len(data.columns))
    for i in range(0, len(data)):#7500
        Lista.append([str(data.values[i,j]) for j in range(0,len(data.columns))])

    Reglas = apriori(Lista, min_support = support, min_confidence = confidence, min_lift = lift, min_length = length)
    Resultados = list(Reglas)
    return Resultados, True
