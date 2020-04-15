# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 23:17:28 2020

@author: duzzi
"""

import pandas as pd
import os
import numpy as np
from datetime import datetime
import random


##cria matriz com dados de treinamento

xtrain_nome = []
xtrain_comp = []
xtrain_cell = []
xtrain = []

xtrain_nome.append("KATE")
xtrain_nome.append("TOM")
xtrain_nome.append("HARRY")
xtrain_nome.append("ANNIKA")
xtrain_nome.append("NAOMI")
xtrain_nome.append("JOE")
xtrain_nome.append("CHAKOTAY")
xtrain_nome.append("NEELIX")
xtrain_nome.append("KES")
xtrain_nome.append("BELANNA")

xtrain_comp.append("PC")
xtrain_comp.append("PC")
xtrain_comp.append("PC")
xtrain_comp.append("MAC")
xtrain_comp.append("MAC")
xtrain_comp.append("MAC")
xtrain_comp.append("MAC")
xtrain_comp.append("MAC")
xtrain_comp.append("PC")
xtrain_comp.append("MAC")

xtrain_cell.append("ANDROID")
xtrain_cell.append("ANDROID")
xtrain_cell.append("ANDROID")
xtrain_cell.append("IPHONE")
xtrain_cell.append("ANDROID")
xtrain_cell.append("IPHONE")
xtrain_cell.append("IPHONE")
xtrain_cell.append("ANDROID")
xtrain_cell.append("IPHONE")
xtrain_cell.append("IPHONE")

xtrain.append(xtrain_nome)
xtrain.append(xtrain_comp)
xtrain.append(xtrain_cell)

Mac_Android = 0
Mac_iphone = 0
PC_Android = 0
PC_iphone = 0

Mac = 0
Pc = 0

## calcula as probabilidades
for j in range(10):
    if xtrain[1][j] == "PC":
        if xtrain[2][j] == "ANDROID":
            PC_Android += 1
        else:
            PC_iphone += 1
        Pc += 1
    else:
        if xtrain[2][j] == "ANDROID":
            Mac_Android += 1
        else:
            Mac_iphone += 1            
        Mac += 1
        
Mac_Android = Mac_Android/Mac
Mac_iphone = Mac_iphone/Mac
PC_Android = PC_Android/Pc 
PC_iphone = PC_iphone/Pc

resp_ok = 0
## coloca input para usuario indicar qual computador possui
while resp_ok == 0:
    computador_cliente = input("qual seu computador (MAC = 1, PC = 2):")
    if computador_cliente == "1" or computador_cliente == "2":
        resp_ok=1
    else:
        print("Digitado errado, favor corrigir")
        
## resposta mediante classificador

if computador_cliente == "1":
    if Mac_Android > Mac_iphone:
        print("VÔCE POSSUI UM MAC E DEVE COMPRAR UM ANDROID")
    elif Mac_iphone > Mac_Android:
        print("VÔCE POSSUI UM MAC E DEVE COMPRAR UM IPHONE")
    else:
        print("VOCÊ POSSUI UM MAC E DECIDE QUAL CELULAR COMPRAR")
        
if computador_cliente == "2":
    if PC_Android > PC_iphone:
        print("VÔCE POSSUI UM PC E DEVE COMPRAR UM ANDROID")
    elif PC_iphone > PC_Android:
        print("VÔCE POSSUI UM PC E DEVE COMPRAR UM IPHONE")
    else:
        print("VOCÊ POSSUI UM PC E DECIDE QUAL CELULAR COMPRAR")


