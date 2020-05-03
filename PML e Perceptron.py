# -*- coding: utf-8 -*-
"""
Created on Sun May  3 14:29:05 2020

@author: duzzi
"""

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import numpy.linalg as la 
from random import randint
import math
from sklearn.datasets import load_iris
import random
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier

IRIS_prob = load_iris()
dados = IRIS_prob.data
result = IRIS_prob.target
result = np.reshape(result,(150,1))

##separa dados de treinamento dos dados de validação  3 classes
dados_treinamento = dados[0:40,:].copy()
dados_treinamento = np.append(dados_treinamento.copy(),dados[50:90,:].copy(),axis=0)
dados_treinamento = np.append(dados_treinamento.copy(),dados[100:140,:].copy(),axis=0)
result_treinamento = result[0:40,:].copy()
result_treinamento = np.append(result_treinamento.copy(),result[50:90,:].copy(),axis=0)
result_treinamento = np.append(result_treinamento.copy(),result[100:140,:].copy(),axis=0)

dados_valid = dados[40:50,:].copy()
dados_valid = np.append(dados_valid.copy(),dados[90:100,:].copy(),axis=0)
dados_valid = np.append(dados_valid.copy(),dados[140:150,:].copy(),axis=0)
result_valid = result[40:50,:].copy()
result_valid = np.append(result_valid.copy(),result[90:100,:].copy(),axis=0)
result_valid = np.append(result_valid.copy(),result[140:150,:].copy(),axis=0)

##separa dados de treinamento dos dados de validação  2 classes
dados_treinamento_2c = dados[0:40,:].copy()
dados_treinamento_2c = np.append(dados_treinamento_2c.copy(),dados[50:90,:].copy(),axis=0)
result_treinamento_2c = result[0:40,:].copy()
result_treinamento_2c = np.append(result_treinamento_2c.copy(),result[50:90,:].copy(),axis=0)

dados_valid_2c = dados[40:50,:].copy()
dados_valid_2c = np.append(dados_valid_2c.copy(),dados[90:100,:].copy(),axis=0)
result_valid_2c = result[40:50,:].copy()
result_valid_2c = np.append(result_valid_2c.copy(),result[90:100,:].copy(),axis=0)

result_treinamento = np.reshape(result_treinamento,(120,))
result_treinamento_2c = np.reshape(result_treinamento_2c,(80,))

##PERCEPTRON PARA DUAS CLASSES
clf_P2 = Perceptron(tol=1e-3, random_state=0)
pesos_P2 = clf_P2.fit(dados_treinamento_2c,result_treinamento_2c)

result_P2 = clf_P2.predict(dados_valid_2c)
##compara dados reais com classificação do Perceptron
aux = 0
for i in range(len(result_valid_2c)):
    if result_P2[i] == result_valid_2c[i,0]:
        aux +=1

Acerto_P2 = (aux/len(result_valid_2c))*100


##PERCEPTRON PARA 3 CLASSES
clf_P3 = Perceptron(tol=1e-3, random_state=0)
pesos_P3 = clf_P3.fit(dados_treinamento,result_treinamento)

result_P3 = clf_P3.predict(dados_valid)
##compara dados reais com classificação do Perceptron
aux = 0
for i in range(len(result_valid)):
    if result[i] == result_valid[i,0]:
        aux +=1

Acerto_P3 = (aux/len(result_valid))*100

##MLP

clf_MLP = MLPClassifier(solver='lbfgs', alpha=1e-2, hidden_layer_sizes=(7,14), random_state=1, max_iter = 300000)
pesos_MPL = clf_MLP.fit(dados_treinamento, result_treinamento)

result_MLP = clf_MLP.predict(dados_valid)

##compara dados reais com classificação do MLP
aux = 0
for i in range(len(result_valid)):
    if result_MLP[i] == result_valid[i,0]:
        aux +=1

Acerto_MLP = (aux/len(result_valid))*100

print("Acerto Perceptro 2 classes:")
print(Acerto_P2)
print("Acerto Perceptro 3 classes:")
print(Acerto_P3)
print("Acerto MLP 3 classes:")
print(Acerto_MLP)


