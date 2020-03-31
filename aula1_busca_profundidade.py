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
aux_profund = 0

# _________________________________________
#Busca por profundidade
#__________________________________________
resultado = 0

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

while Elementos != [] and resultado == 0:

    #busca os nós filhos e verifica se algum deles é a soluçao ou se já foi visitado
    # buscas os nós filhos executando as possiveis manobras  
    while 1:
        valor = enche3l(Elementos[aux_profund])
        resultado = eobjetivo(valor)
        if resultado == 0:
            if valor in Elementos:
                if valor in Visitados:
                    break
                else:
                    Visitados.append(valor)
                    Camada_Aux.append(Elementos[aux_profund])
            else:
                if valor in Visitados:
                    0
                else:
                    Visitados.append(valor)
                    Camada_Aux.append(Elementos[aux_profund])
                    Elementos.append(valor)
                    aux_profund = aux_profund + 1
               
        else:
            Visitados.append(valor)
            Camada_Aux.append(Elementos[aux_profund])
            Elementos.append(valor)
            break
   
    if resultado == 1:
        break
            
    while 1:
        valor = enche4l(Elementos[aux_profund])
        resultado = eobjetivo(valor)
        if resultado == 0:
            if valor in Elementos:
                if valor in Visitados:
                    break
                else:
                    Visitados.append(valor)
                    Camada_Aux.append(Elementos[aux_profund])
            else:
                if valor in Visitados:
                    0
                else:
                    Visitados.append(valor)
                    Camada_Aux.append(Elementos[aux_profund])
                    Elementos.append(valor)
                    aux_profund = aux_profund + 1
               
        else:
            Visitados.append(valor)
            Camada_Aux.append(Elementos[aux_profund])
            Elementos.append(valor)
            break
   
    if resultado == 1:
        break
       
    while 1:
        valor = esvazia3l(Elementos[aux_profund])
        resultado = eobjetivo(valor)
        if resultado == 0:
            if valor in Elementos:
                if valor in Visitados:
                    break
                else:
                    Visitados.append(valor)
                    Camada_Aux.append(Elementos[aux_profund])
            else:
                if valor in Visitados:
                    0
                else:
                    Visitados.append(valor)
                    Camada_Aux.append(Elementos[aux_profund])
                    Elementos.append(valor)
                    aux_profund = aux_profund + 1
               
        else:
            Visitados.append(valor)
            Camada_Aux.append(Elementos[aux_profund])
            Elementos.append(valor)
            break
   
    if resultado == 1:
        break

    while 1:
        valor = esvazia4l(Elementos[aux_profund])
        resultado = eobjetivo(valor)
        if resultado == 0:
            if valor in Elementos:
                if valor in Visitados:
                    break
                else:
                    Visitados.append(valor)
                    Camada_Aux.append(Elementos[aux_profund])
            else:
                if valor in Visitados:
                    0
                else:
                    Visitados.append(valor)
                    Camada_Aux.append(Elementos[aux_profund])
                    Elementos.append(valor)
                    aux_profund = aux_profund + 1
               
        else:
            Visitados.append(valor)
            Camada_Aux.append(Elementos[aux_profund])
            Elementos.append(valor)
            break
   
    if resultado == 1:
        break
            
    while 1:
        valor = transf_3lto4l(Elementos[aux_profund])
        resultado = eobjetivo(valor)
        if resultado == 0:
            if valor in Elementos:
                if valor in Visitados:
                    break
                else:
                    Visitados.append(valor)
                    Camada_Aux.append(Elementos[aux_profund])
            else:
                if valor in Visitados:
                    0
                else:
                    Visitados.append(valor)
                    Camada_Aux.append(Elementos[aux_profund])
                    Elementos.append(valor)
                    aux_profund = aux_profund + 1
               
        else:
            Visitados.append(valor)
            Camada_Aux.append(Elementos[aux_profund])
            Elementos.append(valor)
            break
   
    if resultado == 1:
        break

    while 1:
        valor = transf_4lto3l(Elementos[aux_profund])
        resultado = eobjetivo(valor)
        if resultado == 0:
            if valor in Elementos:
                if valor in Visitados:
                    aux_profund = aux_profund - 1
                    break
                else:
                    Visitados.append(valor)
                    Camada_Aux.append(Elementos[aux_profund])
            else:
                if valor in Visitados:
                    0
                else:
                    Visitados.append(valor)
                    Camada_Aux.append(Elementos[aux_profund])
                    Elementos.append(valor)
                    aux_profund = aux_profund + 1
               
        else:
            Visitados.append(valor)
            Camada_Aux.append(Elementos[aux_profund])
            Elementos.append(valor)
            break
   
    if resultado == 1:
        break
   
        #caso o resultado seja zero para todos os casos, o valor aux profundidade volta para o ultimo elemento pai e busca novamente a partir dali
        #deixando o laço while rodar até encontrar solução


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

