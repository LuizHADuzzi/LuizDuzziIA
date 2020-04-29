# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 20:41:39 2020

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
from sklearn.linear_model import LinearRegression
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn import svm
from mpl_toolkits.mplot3d import Axes3D

IRIS_prob = load_iris()
dados = IRIS_prob.data
result = IRIS_prob.target
## regressao linear - sepal length x sepal width
lr = LinearRegression()
x_train = dados[:,0].copy()
x_train = x_train.reshape(150,1)
y_train = dados[:,2].copy()
y_train = y_train.reshape(150,1)

lr.fit(x_train, y_train)

Y_pred_LR_1 = lr.predict(x_train)
X_pred_LR_1 = x_train.copy()

## regressao linear - petal length x petal width
x_train = dados[:,2].copy()
x_train = x_train.reshape(150,1)
y_train = dados[:,3].copy()
y_train = y_train.reshape(150,1)

lr.fit(x_train, y_train)

Y_pred_LR_2 = lr.predict(x_train)
X_pred_LR_2 = x_train.copy()


plt.figure(figsize = (10,10))
plt.subplot(2,2,1)
plt.title("Regressão Linear")
plt.plot(X_pred_LR_1,Y_pred_LR_1, label='Sepal Predict') 
plt.plot(X_pred_LR_2,Y_pred_LR_2, label='Petal Predict')
plt.plot(dados[:,0], dados[:,1], 'go',label='Sepal Data') 
plt.plot(dados[:,2], dados[:,3], 'bo',label='Petal Data')  
plt.legend()
plt.grid(True)

## PCA
dados_PCA = dados.copy()
pca = PCA(n_components = 2)
pca.fit(dados_PCA)
dados_PCA_transf = pca.transform(dados_PCA)

plt.subplot(2,2,2)
plt.title("PCA")
plt.plot(dados_PCA_transf[:,0], dados_PCA_transf[:,1], 'go',label='PCA transf') 
plt.legend()
plt.grid(True)

## LDA
dados_LDA = dados.copy()
result_LDA = result.copy()
clf = LDA(n_components = 2)
clf.fit(dados_LDA,result_LDA)

dados_LDA_transf = clf.transform(dados_LDA)
LDA_predict = clf.predict(dados_LDA)

plt.subplot(2,2,3)
plt.title("LDA")
for i in range(len(LDA_predict)):
    if LDA_predict[i] == 0:
        plt.plot(dados_LDA_transf[i,0], dados_LDA_transf[i,1], 'go') 
    if LDA_predict[i] == 1:
        plt.plot(dados_LDA_transf[i,0], dados_LDA_transf[i,1], 'bo') 
    if LDA_predict[i] == 2:
        plt.plot(dados_LDA_transf[i,0], dados_LDA_transf[i,1], 'ro') 

plt.plot(0, 0, 'go',label='LDA transf - Setosa') 
plt.plot(0, 0, 'bo',label='LDA transf - Versicolor') 
plt.plot(0, 0, 'ro',label='LDA transf - Virginica') 
plt.legend()
plt.grid(True)

## SVM

dados_SVM = dados[:,:2].copy() ##somente duas classes para plotar em 2D
result_SVM = result.copy()

clf_svm = svm.SVC(kernel = "rbf", gamma = "auto")
clf_svm.fit(dados_SVM,result_SVM)

svm_predict = clf_svm.predict(dados_SVM)

plt.subplot(2,2,4)
plt.title("SVM")
for i in range(len(svm_predict)):
    if svm_predict[i] == 0:
        plt.plot(dados_SVM[i,0], dados_SVM[i,1], 'go') 
    if svm_predict[i] == 1:
        plt.plot(dados_SVM[i,0], dados_SVM[i,1], 'bo') 
    if svm_predict[i] == 2:
        plt.plot(dados_SVM[i,0], dados_SVM[i,1], 'ro') 
plt.plot(0, 0, 'go',label='SVM transf - Setosa') 
plt.plot(0, 0, 'bo',label='SVM transf - Versicolor') 
plt.plot(0, 0, 'ro',label='SVM transf - Virginica') 
plt.legend()
plt.grid(True)








