# -*- coding: utf-8 -*-
"""
Spyder Editor

Autor: Luiz Henrique Alves Duzz
Prof: Reinaldo Bianchi
PEL 202 - Fundamentos de IA

"""

import pandas as pd
import os
import numpy as np

# define funções possiveis

# a entrada das funções é um vetor contendo [jarra3l , jarra4l]
# Enche 3L
def enche3l(jarravetor):
    j3lf = 3
    j4lf = jarravetor[1]
    return [j3lf,j4lf];

# Enche 4L
def enche4l(jarravetor):
    j4lf = 4
    j3lf = jarravetor[0]

    return [j3lf,j4lf];

# Esvazia 3L
def esvazia3l(jarravetor):
    j3lf = 0
    j4lf = jarravetor[1]

    return [j3lf,j4lf];

# Esvazia 4L
def esvazia4l(jarravetor):
    j4lf = 0
    j3lf = jarravetor[0]

    return [j3lf,j4lf];

# Transfere 3 para 4 litros
def transf_3lto4l(jarravetor):
    j4lf = jarravetor[0] + jarravetor[1]
    j3lf = 0
    if j4lf > 4:
        j3lf = j4lf - 4
        j4lf = 4

    return [j3lf,j4lf];

# Transfere 4 para 3 litros
def transf_4lto3l(jarravetor):
    j3lf = jarravetor[0] + jarravetor[1]
    j4lf = 0
    if j3lf > 3:
        j4lf = j3lf - 3
        j3lf = 3

    return [j3lf,j4lf];


#Define Objetivo, o exercicio fala que deve conter 2 L no jarro de 4 L, não fala nenhum valor no de 3L, por isso existem 4 possiveis
#objetivos, o programar irá parar quando achar qualquer um deles.
def eobjetivo(elementos):   
    objetivo1 = [0,2]
    objetivo2 = [1,2]
    objetivo3 = [2,2]
    objetivo4 = [3,2]
    
    resultado = 0
    
    if objetivo1 == elementos:
        resultado = 1
    if objetivo2 == elementos:
        resultado = 1
    if objetivo3 == elementos:
        resultado = 1
    if objetivo4 == elementos:
        resultado = 1
      
    return resultado;
                  
Visitados=[]
Elementos=[]
Camada_Aux=[]
#Define Estado Inicial
valor = [0,0]

# _________________________________________
#Busca por largura
#__________________________________________
resultado = 0
camada = 0

resultado = eobjetivo(valor)
if resultado == 0:
    if valor in Elementos:
        if valor in Visitados:
            0
        else:
            Visitados.append(valor)
           
    else:
        Elementos.append(valor)
        if valor in Visitados:
            0
        else:
            Visitados.append(valor)

while Elementos != [] and resultado == 0 :

    #busca os nós filhos e verifica se algum deles é a soluçao ou se já foi visitado

    # buscas os nós filhos executando as possiveis manobras (tira o elemento pai da fila e envia para visitados)   
    valor = enche3l(Elementos[0])
    resultado = eobjetivo(valor)
    if resultado == 0:
        if valor in Elementos:
            if valor in Visitados:
                0
            else:
                Visitados.append(valor)
                Camada_Aux.append(Elementos[0])
        else:
            if valor in Visitados:
                0
            else:
                Visitados.append(valor)
                Camada_Aux.append(Elementos[0])
                Elementos.append(valor)
    else:
        Visitados.append(valor)
        Camada_Aux.append(Elementos[0])
        Elementos.append(valor)
        break
            
    valor = enche4l(Elementos[0])
    resultado = eobjetivo(valor)
    if resultado == 0:
        if valor in Elementos:
            if valor in Visitados:
                0
            else:
                Visitados.append(valor)
                Camada_Aux.append(Elementos[0])
        else:
            if valor in Visitados:
                0
            else:
                Visitados.append(valor)
                Camada_Aux.append(Elementos[0])
                Elementos.append(valor)
    else:
        Visitados.append(valor)
        Camada_Aux.append(Elementos[0])
        Elementos.append(valor)
        break
            
    valor = esvazia3l(Elementos[0])
    resultado = eobjetivo(valor)
    if resultado == 0:
        if valor in Elementos:
            if valor in Visitados:
                0
            else:
                Visitados.append(valor)
                Camada_Aux.append(Elementos[0])
        else:
            if valor in Visitados:
                0
            else:
                Visitados.append(valor)
                Camada_Aux.append(Elementos[0])
                Elementos.append(valor)
    else:
        Visitados.append(valor)
        Camada_Aux.append(Elementos[0])
        Elementos.append(valor)
        break

    valor = esvazia4l(Elementos[0])
    resultado = eobjetivo(valor)
    if resultado == 0:
        if valor in Elementos:
            if valor in Visitados:
                0
            else:
                Visitados.append(valor)
                Camada_Aux.append(Elementos[0])
        else:
            if valor in Visitados:
                0
            else:
                Visitados.append(valor)
                Camada_Aux.append(Elementos[0])
                Elementos.append(valor)
    else:
        Visitados.append(valor)
        Camada_Aux.append(Elementos[0])
        Elementos.append(valor)
        break
            
    valor = transf_3lto4l(Elementos[0])
    resultado = eobjetivo(valor)
    if resultado == 0:
        if valor in Elementos:
            if valor in Visitados:
                0
            else:
                Visitados.append(valor)
                Camada_Aux.append(Elementos[0])
        else:
            if valor in Visitados:
                0
            else:
                Visitados.append(valor)
                Camada_Aux.append(Elementos[0])
                Elementos.append(valor)
    else:
        Visitados.append(valor)
        Camada_Aux.append(Elementos[0])
        Elementos.append(valor)
        break

    valor = transf_4lto3l(Elementos[0])
    resultado = eobjetivo(valor)
    if resultado == 0:
        if valor in Elementos:
            if valor in Visitados:
                0
            else:
                Visitados.append(valor)
                Camada_Aux.append(Elementos[0])
        else:
            if valor in Visitados:
                0
            else:
                Visitados.append(valor)
                Camada_Aux.append(Elementos[0])
                Elementos.append(valor)
    else:
        Visitados.append(valor)
        Camada_Aux.append(Elementos[0])
        Elementos.append(valor)
        break
        #caso o resultado seja zero para todos os casos, o valor procurado ainda nao foi achado, assim o elemento inicial sai da fila
        #deixando o laço while rodar até encontrar solução, ou até acabar a quantidade de elementos na fila principal
    Elementos.pop(0)    

#cria uma lista com o resuntado
Resultado = []    

stop = 0

Resultado.append(valor)
while stop == 0 :
    
    
    index = Visitados.index(valor)
    if index == 0:
        stop = 1
        break
    Resultado.append(Camada_Aux[index-1])
    valor = Camada_Aux[index-1]

Resultado.reverse()

