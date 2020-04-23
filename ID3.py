# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:53:36 2020

@author: duzzi
"""

import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
import numpy.linalg as la 
from random import randint
import math
from sklearn.datasets import load_iris
import random

def Teste_grupo(dados):
    if len(dados)>0:
        aux_0 = 0
        aux_1 = 0
        aux_2 = 0
        for i in range(len(dados)):
            if dados[i,4] == 0:
                aux_0 = aux_0 + 1
            elif dados[i,4] == 1:
                aux_1 =aux_1+ 1
            elif dados[i,4] == 2:
                aux_2 =aux_2+1
        #print(aux_0/len(dados))
        #print(aux_1/len(dados))
        #print(aux_2/len(dados))
        if aux_0/len(dados) >= 0.62:
            return 0, aux_0, aux_1, aux_2
        elif aux_1/len(dados) >= 0.62:
            return 1, aux_0, aux_1, aux_2
        elif aux_2/len(dados) >= 0.62:
            return 2, aux_0, aux_1, aux_2
        else:
            return 3, aux_0, aux_1, aux_2
    else:
        return 3, aux_0, aux_1, aux_2
    
def separa_grupos(media,dados,coluna):
    aux_maior = np.zeros((1,5))
    aux_menor = np.zeros((1,5))
    for j in range(len(dados)):
        if medias[0,coluna] > dados[j,coluna]:
            aux_menor = np.append(aux_menor,np.resize(dados[j,:],(1,5)),axis=0)
        else:
            aux_maior = np.append(aux_maior,np.resize(dados[j,:],(1,5)),axis=0)
    aux_maior = np.delete(aux_maior,0,axis=0)
    aux_menor = np.delete(aux_menor,0,axis=0)
    return aux_maior,aux_menor
       
IRIS_prob = load_iris()
dados = IRIS_prob.data
result = IRIS_prob.target

## calculando Entropia
H_total = -1*((1/3)*math.log2(1/3)+(1/3)*math.log2(1/3)+(1/3)*math.log2(1/3))

## tira media dos valores de comprimento e largura da sepala e petala

linhas, col = dados.shape

medias = np.zeros([1,col])
valores_media = np.zeros([8,col])

for i in range(col):
    medias[0,i] = np.mean(dados[:,i])
    
## verifica quanto valores estao abaixo das medias e acima das medias

for i in range(col):
    aux_maior = 0
    aux_menor = 0
    aux_tp1_ma = 0
    aux_tp2_ma = 0
    aux_tp0_ma = 0
    aux_tp1_me = 0
    aux_tp2_me = 0
    aux_tp0_me = 0
    for j in range(linhas):
        if medias[0,i] > dados[j,i]:
            aux_maior = aux_maior + 1
            if result[j] == 0:
                aux_tp0_ma = aux_tp0_ma + 1
            if result[j] == 1:
                aux_tp1_ma = aux_tp1_ma + 1
            if result[j] == 2:
                aux_tp2_ma = aux_tp2_ma + 1
        else:
            aux_menor = aux_menor + 1
            if result[j] == 0:
                aux_tp0_me = aux_tp0_me + 1
            if result[j] == 1:
                aux_tp1_me = aux_tp1_me + 1
            if result[j] == 2:
                aux_tp2_me = aux_tp2_me + 1
    valores_media[0,i] = aux_maior
    valores_media[1,i] = aux_tp0_ma
    valores_media[2,i] = aux_tp1_ma
    valores_media[3,i] = aux_tp2_ma   
    valores_media[4,i] = aux_menor
    valores_media[5,i] = aux_tp0_me
    valores_media[6,i] = aux_tp1_me
    valores_media[7,i] = aux_tp2_me  
    
##calculo entropia condicional
    
H_condicional = np.ones(4)
for i in range(col):
    aux_maior = 0
    aux_menor = 0
    for j in range(1,4):
        if valores_media[j,i] == 0:
            aux_maior = aux_maior
        else:
            aux_maior = aux_maior + (valores_media[j,i]/valores_media[0,i])*math.log2(valores_media[j,i]/valores_media[0,i])  
    for j in range(5,8):
        if valores_media[j,i] == 0:
            aux_menor = aux_menor
        else:
            aux_menor = aux_menor + (valores_media[j,i]/valores_media[4,i])*math.log2(valores_media[j,i]/valores_media[4,i])  
    H_condicional[i] = -((valores_media[4,i]/linhas)*aux_menor + (valores_media[0,i]/linhas)*aux_maior)

#calculo do Information Gain

IG_final = []

for i in range(col):
    IG_final.append(H_total - H_condicional[i])
    
## monta arvore baseado nos valores de information gain, quanto maior mais significante é para realizar a separaçao
folhas = [] # index na sequencia que deve ser utilizado
for i in range(col):
    folhas.append(IG_final.index(max(IG_final)))
    IG_final[IG_final.index(max(IG_final))] = 0

aux_result = np.zeros((150,1))

for i in range(linhas):
    aux_result[i,0] = result[i]
    
dados_target = np.concatenate((dados.copy(),aux_result.copy()),axis = 1)

i=0
## faz a separeçao em grupos de acordo com as medias e define cada classe (treinamento) construindo a matriz arvore
#nó1
aux_maior_A, aux_menor_A = separa_grupos(medias,dados_target.copy(),folhas[i])
arvore = np.zeros((10,8))
arvore[0,0] = 1 #dados maiores que a media
arvore[1,0] = 0 #dados menores que a media 
arvore[0,1] = folhas[0]
arvore[1,1] = folhas[0]
arvore[0,2] = medias[0,folhas[0]]
arvore[1,2] = medias[0,folhas[0]]  
# se a media for menor do que o erro informa a classe, caso contrario realiza a proxima varredura na proxima folha
arvore[0,3],arvore[0,4],arvore[0,5],arvore[0,6] = Teste_grupo(aux_maior_A)
arvore[1,3],arvore[1,4],arvore[1,5],arvore[1,6] = Teste_grupo(aux_menor_A)


#nó2
aux_maior_B, aux_menor_m_B = separa_grupos(medias,aux_maior_A.copy(),folhas[2])
arvore[2,3],arvore[2,4],arvore[2,5],arvore[2,6] = Teste_grupo(aux_maior_B)
arvore[3,3],arvore[3,4],arvore[3,5],arvore[3,6] = Teste_grupo(aux_menor_m_B)
arvore[2,0] = 1 #dados maiores que a media
arvore[2,1] = folhas[2]
arvore[2,2] = medias[0,folhas[2]]
arvore[2,7] = medias[0,folhas[0]]
arvore[3,0] = 0 #dados menores que a media
arvore[3,1] = folhas[2]
arvore[3,2] = medias[0,folhas[2]]
arvore[3,7] = medias[0,folhas[0]]
  

#nó3
aux_maior_m_C, aux_menor_C = separa_grupos(medias,aux_menor_A.copy(),folhas[3])
arvore[4,3],arvore[4,4],arvore[4,5],arvore[4,6] = Teste_grupo(aux_maior_m_C)
arvore[4,0] = 1 #dados maiores que a media
arvore[4,1] = folhas[3]
arvore[4,2] = medias[0,folhas[3]]
arvore[4,7] = medias[0,folhas[0]]
arvore[5,3],arvore[5,4],arvore[5,5],arvore[5,6] = Teste_grupo(aux_menor_C)
arvore[5,0] = 0 #dados menores que a media
arvore[5,1] = folhas[3]
arvore[5,2] = medias[0,folhas[3]]
arvore[5,7] = medias[0,folhas[0]]

#nó4
aux_maior_D, aux_menor_m_D = separa_grupos(medias,aux_maior_B.copy(),folhas[1])
arvore[6,3],arvore[6,4],arvore[6,5],arvore[6,6] = Teste_grupo(aux_maior_D)
arvore[6,0] = 1 #dados maiores que a media
arvore[6,1] = folhas[1]
arvore[6,2] = medias[0,folhas[1]]
arvore[6,7] = medias[0,folhas[2]]
arvore[7,3],arvore[7,4],arvore[7,5],arvore[7,6] = Teste_grupo(aux_menor_m_D)
arvore[7,0] = 0 #dados menores que a media
arvore[7,1] = folhas[1]
arvore[7,2] = medias[0,folhas[1]]
arvore[7,7] = medias[0,folhas[2]]

#nó5
aux_maior_m_E, aux_menor_E = separa_grupos(medias,aux_menor_C.copy(),folhas[1])
arvore[8,3],arvore[8,4],arvore[8,5],arvore[8,6] = Teste_grupo(aux_maior_m_E)
arvore[8,0] = 1 #dados maiores que a media
arvore[8,1] = folhas[1]
arvore[8,2] = medias[0,folhas[1]]
arvore[8,7] = medias[0,folhas[3]]
arvore[9,3],arvore[9,4],arvore[9,5],arvore[9,6] = Teste_grupo(aux_menor_E)
arvore[9,0] = 0 #dados menores que a media
arvore[9,1] = folhas[1]
arvore[9,2] = medias[0,folhas[1]]
arvore[9,7] = medias[0,folhas[3]]

### com a arvore criada, realizar testes
resposta_arvore = np.zeros((len(dados),1))
for i in range(len(dados)):
    if arvore[0,2] < dados[i,2]:
        if arvore[2,2] < dados[i,0]:
            if arvore[6,2] < dados[i,3]:
                resposta_arvore[i,0]=arvore[6,3]
            else:
                resposta_arvore[i,0]=arvore[8,3]
        else:
            resposta_arvore[i,0]=arvore[3,3]
    else:
        if arvore[4,2] < dados[i,1]:
            resposta_arvore[i,0]=arvore[4,3]
        else:
            if arvore[7,2] < dados[i,3]:
                resposta_arvore[i,0]=arvore[7,3]
            else:
                resposta_arvore[i,0]=arvore[4,3]


