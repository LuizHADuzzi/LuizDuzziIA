# -*- coding: utf-8 -*-
"""
Created on Tue May 26 21:03:40 2020

@author: duzzi
"""
import pandas as pd
import os
from numpy import exp, array, random, dot
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
import numpy.linalg as la 
from random import sample
import math
from collections import Counter
import numpy as np

def acao_rand(estado_atual,aux):
        
    ##considerando os estados da sequinte maneira:
    
    #_____________
    #|   |   |   |
    #| 0 | 2 | 4 |
    #|   |   |   |
    #|____________
    #|   |   |   |
    #| 1 | 3 | 5 |
    #|   |   |   |
    #_____________
    
    if estado_atual == 0:
        if aux == 0 or aux == 2:
            acao = 1
        else:
            acao = 2
        recompensa = 0
        if acao == 1:
            novo_estado = 1
        elif acao == 2:
            novo_estado = 2
            
    elif estado_atual == 1:
        if aux == 0 or aux == 2:
            acao = 0
        else:
            acao = 3
        recompensa = 0
        if acao == 0:
            novo_estado = 0
        elif acao == 3:
            novo_estado = 3
            
    elif estado_atual == 2:
        if aux == 0:
            acao = 0
        elif aux == 1:
            acao = 3
        else:
            acao = 4
        if acao == 3:
            novo_estado = 3
            recompensa = 0
        elif acao == 4:
            novo_estado = 4
            recompensa = 100
        elif acao == 0:
            novo_estado = 0
            recompensa = 0
            
    elif estado_atual == 3:
        if aux == 0:
            acao = 1
        elif aux == 1:
            acao = 2
        else:
            acao = 5
        recompensa = 0
        if acao == 2:
            novo_estado = 2
        elif acao == 5:
            novo_estado = 5
        elif acao == 1:
            novo_estado = 1
            
    elif estado_atual ==4:
        acao = 4 # loop
        recompensa = 0
        novo_estado = 4
            
    elif estado_atual == 5:
        if aux == 0:
            acao = 4
        else:
            acao = 3
        if acao == 4:
            novo_estado = 4
            recompensa = 100
        elif acao == 3:
            novo_estado = 3
            recompensa = 0
           
    return novo_estado, acao, recompensa



def maximo_Q(Q,estado):
    global maximo
    
    if estado == 0:
        maximo = max(Q[0,2],Q[0,1])
        
    elif estado == 1:
        maximo = max(Q[1,0],Q[1,3])

    elif estado == 2:
        maximo = max(Q[2,0],Q[2,3],Q[2,4])
        
    elif estado == 3:
        maximo = max(Q[3,1],Q[3,2],Q[3,5])
    
    elif estado == 4:
        maximo = 0
        
    elif estado == 5:
        maximo = max(Q[5,4],Q[5,3]) 
    
    return maximo
    
Gama = 0.9
taxa_apr = 0.1

s = [0,1,2,3,4,5]
a = [0,1,2,3,4,5]

##Inicia a tabela Q em 0
Q=np.zeros((len(s),len(a)))

aux = 0
estado_inicial = 0
aux_acao = 0
while aux <= 300:
    
    while aux_acao <= 3:
    
        s_linha, acao, rec = acao_rand(estado_inicial,aux_acao) # executa uma acao randomica
            
        Q_max = maximo_Q(Q,s_linha)

        
        Q[estado_inicial,acao] = (1-taxa_apr)*Q[estado_inicial,acao] + taxa_apr*(rec + Gama * Q_max)
        
        aux_acao = aux_acao + 1
    
    aux = aux + 1
    
    estado_inicial = estado_inicial + 1
    if estado_inicial == 6:
        estado_inicial = 0

    aux_acao = 0
    


    
    