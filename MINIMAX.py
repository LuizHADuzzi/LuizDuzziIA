# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 09:54:58 2020

@author: duzzi
"""

import pandas as pd
import os
import numpy as np
from datetime import datetime
import random

## inicio
## cria tabela 3x3 com valores zerados
TABELA = np.zeros((3,3),int)

## X = 1 - usuario
## 0 = -1 - sistema

## funçao para mostrar o tabuleiro e esperar input do usuario
def mostra_tabuleiro(TABELA):    
    for i in range(3):
        for j in range(3):
            if TABELA[i][j] == 0:
                aux = " "
            if TABELA[i][j] == 1:
                aux = "X"
            if TABELA[i][j] == -1:
                aux = "O"
            if j <= 1:
                print (aux, end =" | ")
            else:
                print (aux, end ="\n")
            if i <=1 and j==2:
                print ("_ | _ | _") 
    print("\n \n")
    return()
 
##função para jogada do usuario               
def jogadaX(TABELA): 

    ## verifica se há espaço para jogar
    soma_vazio = 0
    for i in range(3):
        for j in range(3):
            if TABELA[i][j] != 0:
                soma_vazio = soma_vazio + 1
                if soma_vazio == 9:
                    return(TABELA)
    
    erro = 1
    
    while erro == 1:
        
        X = input("Informe o proximo local onde irá  jogar de 1 a 9 (mesma posição do teclado numerico):")  
        print(X)
    ## funçao para atribuir a jogada do usuário ao local correto e verificar se jogada é valida        
        if X == "1":
            if TABELA[2][0]==0:
                TABELA[2][0]=1
                erro = 0
            else:
                print("Posição selecionada invalida, por favor selecione outra jogada")
        elif X == "2":
            if TABELA[2][1]==0:
                TABELA[2][1]=1
                erro = 0
            else:
                print("Posição selecionada invalida, por favor selecione outra jogada")
        elif X == "3":
            if TABELA[2][2]==0:
                TABELA[2][2]=1
                erro = 0
            else:
                print("Posição selecionada invalida, por favor selecione outra jogada")
        elif X == "4":
            if TABELA[1][0]==0:
                TABELA[1][0]=1
                erro = 0
            else:
                print("Posição selecionada invalida, por favor selecione outra jogada")
        elif X == "5":
            if TABELA[1][1]==0:
                TABELA[1][1]=1
                erro = 0
            else:
                print("Posição selecionada invalida, por favor selecione outra jogada")
        elif X == "6":
            if TABELA[1][2]==0:
                TABELA[1][2]=1
                erro = 0
            else:
                print("Posição selecionada invalida, por favor selecione outra jogada")
        elif X == "7":
            if TABELA[0][0]==0:
                TABELA[0][0]=1
                erro = 0
            else:
                print("Posição selecionada invalida, por favor selecione outra jogada")
        elif X == "8":
            if TABELA[0][1]==0:
                TABELA[0][1]=1
                erro = 0
            else:
                print("Posição selecionada invalida, por favor selecione outra jogada")
        elif X == "9":
            if TABELA[0][2]==0:
                TABELA[0][2]=1
                erro = 0
            else:
                print("Posição selecionada invalida, por favor selecione outra jogada")
        else:
            print("Posição selecionada invalida, por favor selecione outra jogada")
        
    return (TABELA)

## funçao minimax para jogada do software        
def jogada0(TABELA):
    
    ## verifica se há espaço para jogar
    soma_vazio = 0
    soma_cheio = 0
    for i in range(3):
        for j in range(3):
            if TABELA[i][j] != 0:
                soma_vazio = soma_vazio + 1
                if soma_vazio == 9:
                    return(TABELA)
            if TABELA[i][j] == 0:
                soma_cheio = soma_cheio + 1
                    
    ##a primeira jogada é randomica
    if soma_cheio == 9:
        a = random.randrange(3)
        b = random.randrange(3)
        
        if TABELA[a][b] == 0:
            TABELA[a][b] = -1
            return(TABELA)
    
    LISTA_JOGADAS0 = []        
    ##faz a verificaçao das proximas jogadas
    LISTA_JOGADAS0 = possiveis_jogadas(TABELA,-1)
    
    aux_possibilidades = len(LISTA_JOGADAS0)
    
    minimo = []
    for i in range(aux_possibilidades):
        aux = possiveis_vitorias(LISTA_JOGADAS0[i])
        minimo.append(aux)    
    
    
    lista_3c = lista_3casos(LISTA_JOGADAS0,minimo)##nao olha para todas as condiçoes, somente as 3 melhores de todas as possiveis (alpha beta)
    
    
    TABELA_BEST = busca_jogada(lista_3c)# olha para os proximos niveis para definir a melhor jogada
            
                
    print(TABELA_BEST)
    
    MELHOR_JOGADA = TABELA + TABELA_BEST

    for i in range(3):
        for j in range(3):
            if MELHOR_JOGADA[i][j] == -1:               
                TABELA[i][j] = -1
    return(TABELA)
    
    

##função verifica ganhador
def verifica_ganhador_semprint(tabuleiro):

    ##verifica vertical
    for i in range(3):
        auxsoma = 0
        auxsoma2 = 0
        for j in range(3):
            auxsoma = auxsoma + tabuleiro[i][j]
            auxsoma2 = auxsoma2 + tabuleiro[j][i]
            if auxsoma == 3 or auxsoma2 == 3:
                #print("VOCÊ GANHOU, PARABENS!!1514")
            
                return 1,1
            elif auxsoma == -3 or auxsoma2 == -3:
                #print("EU GANHEI, TENTE NOVAMENTE!!1515")
                
                return -1,1
                
    ##verifica diagonais
    auxsoma3 = tabuleiro[0][0]+tabuleiro[1][1]+tabuleiro[2][2]
    auxsoma4 = tabuleiro[0][2]+tabuleiro[1][1]+tabuleiro[2][0]
    
    if auxsoma3 == 3 or auxsoma4 == 3:
        #print("VOCÊ GANHOU, PARABENS!!1516")
         
        return 1,1
    elif auxsoma3 == -3 or auxsoma4 == -3:
        #print("EU GANHEI, TENTE NOVAMENTE!!1517")
         
        return -1,1
       
    return 0,0    
    
def verifica_ganhador(tabuleiro):
 
    ##verifica vertical
    for i in range(3):
        auxsoma = 0
        auxsoma2 = 0
        for j in range(3):
            auxsoma = auxsoma + tabuleiro[i][j]
            auxsoma2 = auxsoma2 + tabuleiro[j][i]
            if auxsoma == 3 or auxsoma2 == 3:
                print("VOCÊ GANHOU, PARABENS!!")
            
                return 1,1
            elif auxsoma == -3 or auxsoma2 == -3:
                print("EU GANHEI, TENTE NOVAMENTE!!")
                
                return -1,1
                
    ##verifica diagonais
    auxsoma3 = tabuleiro[0][0]+tabuleiro[1][1]+tabuleiro[2][2]
    auxsoma4 = tabuleiro[0][2]+tabuleiro[1][1]+tabuleiro[2][0]
    
    if auxsoma3 == 3 or auxsoma4 == 3:
        print("VOCÊ GANHOU, PARABENS!!")
         
        return 1,1
    elif auxsoma3 == -3 or auxsoma4 == -3:
        print("EU GANHEI, TENTE NOVAMENTE!!")
         
        return -1,1
       
    return 0,0

def possiveis_vitorias(tabela):
    ##funçao para calcular quantidades de vitorias de X e de 0 e retorna o valor de X-0
    tabela_X = tabela.copy()
    tabela_0 = tabela.copy()
    
    vitorias_X = 0
    vitorias_0 = 0
    
    ##verifica se já houve vitoria de X (10) ou 0 (-10) e vai para o final
    aux_gan,vitoria = verifica_ganhador_semprint(tabela)
    if vitoria == 1:
        if aux_gan == 1:
            return(10)
        else:
            return(-10)        
    
    ##completa o valor das tabelas auxiliar com X ou 0 para verificar as possibilidades de vitoria
    for i in range(3):
        for j in range(3):
            if tabela_X[i][j] == 0:
                tabela_X[i][j] = 1
            if tabela_0[i][j] == 0:
                tabela_0[i][j] = -1
    
    for i in range(3):
        auxsoma_X = 0
        auxsoma2_X = 0
        auxsoma_0 = 0
        auxsoma2_0 = 0
        for j in range(3):
            auxsoma_X = auxsoma_X + tabela_X[i][j]
            auxsoma2_X = auxsoma2_X + tabela_X[j][i]
            auxsoma_0 = auxsoma_0 + tabela_0[i][j]
            auxsoma2_0 = auxsoma2_0 + tabela_0[j][i]
        if auxsoma_X == 3:
            vitorias_X = vitorias_X + 1
        if auxsoma2_X == 3:
            vitorias_X = vitorias_X + 1
        if auxsoma_0 == -3:
            vitorias_0 = vitorias_0 + 1
        if auxsoma2_0 == -3:
            vitorias_0 = vitorias_0 + 1
    
    auxsoma_X = tabela_X[0][0]+tabela_X[1][1]+tabela_X[2][2]
    auxsoma2_X = tabela_X[0][2]+tabela_X[1][1]+tabela_X[2][0]
    auxsoma_0 = tabela_0[0][0]+tabela_0[1][1]+tabela_0[2][2]
    auxsoma2_0 = tabela_0[0][2]+tabela_0[1][1]+tabela_0[2][0]
    
    if auxsoma_X == 3:
        vitorias_X = vitorias_X + 1
    if auxsoma2_X == 3:
        vitorias_X = vitorias_X + 1
    if auxsoma_0 == -3:
        vitorias_0 = vitorias_0 + 1
    if auxsoma2_0 == -3:
        vitorias_0 = vitorias_0 + 1
    
    return(vitorias_X-vitorias_0)

def possiveis_jogadas(tabela,quemjoga):
    ##funçao que retorna uma lista para todas as possiveis proximas jogadas do computador (0)
    tabela_LISTA = []
    aux_posicao = []
    aux_TABELA = tabela.copy()
    
    for i in range(3):
        for j in range(3):
            if aux_TABELA[i][j] == 0:
                if [i,j] in aux_posicao:
                    0
                else:
                    if quemjoga == -1:
                        aux_TABELA[i][j] = -1
                    else:
                        aux_TABELA[i][j] = 1
                    tabela_LISTA.append(aux_TABELA.copy())
                    aux_TABELA = tabela.copy()
                    aux_posicao.append([i,j])
    return(tabela_LISTA)

def lista_3casos(lista_tabela,vetor_vitoria):
    
    aux = len(lista_tabela)
    if aux < 3:
        return(lista_tabela)
    else:
        aux_vetor = vetor_vitoria.copy()
        aux_vetor.sort()
        vetor_index = []  
        for j in range(3):
            for i, item in enumerate(vetor_vitoria): 
                if item == aux_vetor[j]:
                    if i in vetor_index:
                        0
                    else:
                        vetor_index.append(i)

        
        lista_3c = []
        for i in range(3):
            lista_3c.append(lista_tabela[vetor_index[i]])
        return(lista_3c)
        
def busca_jogada(lista_melhores0):
    
    Lista_X = []
    Lista_0 = []
    Result_jogadas_0 = []
    if len(lista_melhores0) == 1:
        
        return(lista_melhores0[0])

   
    elif len(lista_melhores0) == 2:
        
        aux0 = possiveis_vitorias(lista_melhores0[0])
        aux1 = possiveis_vitorias(lista_melhores0[1])
        
        if aux0-aux1>=0:
            return(lista_melhores0[0])
        else:
            return(lista_melhores0[1])
            
    elif len(lista_melhores0) == 3:
        Lista_X1 = possiveis_jogadas(lista_melhores0[0],1)
        Lista_X2 = possiveis_jogadas(lista_melhores0[1],1)
        Lista_X3 = possiveis_jogadas(lista_melhores0[2],1)
        Lista_X.append(Lista_X1.copy())
        Lista_X.append(Lista_X2.copy())
        Lista_X.append(Lista_X3.copy())

    
        
    for i in range(len(Lista_X)):
        for j in range(len(Lista_X[i])):
            aux_Jogadas_0 = possiveis_jogadas(Lista_X[i][j],-1)
            Lista_0.append(aux_Jogadas_0.copy())
        
    for i in range(len(Lista_0)):
        for j in range(len(Lista_0[i])):
            aux = possiveis_vitorias(Lista_0[i][j])
            Result_jogadas_0.append(aux)



    divisao = len(Result_jogadas_0)/len(lista_melhores0)

    r_index = Result_jogadas_0.index(min(Result_jogadas_0))
    print(Result_jogadas_0)
    print(r_index)        
    if r_index <= divisao:
        return(lista_melhores0[0])
    elif r_index > divisao and r_index <=divisao*2:
        return(lista_melhores0[1])
    else:
        return(lista_melhores0[2])

        
    

    
    
##___________________________________________________________________________________
## programa principal
auxinicio = 0
ganhador = 0
fim = 1
TABELA = np.zeros((3,3),int)
jogadas = 0
while fim == 1:
        
    while ganhador == 0:
        
        if auxinicio == 0: ## Usuario começa           
            mostra_tabuleiro(TABELA)
            TABELA = jogadaX(TABELA)
            aux, ganhador = verifica_ganhador(TABELA)
            if ganhador == 1:
                mostra_tabuleiro(TABELA)
                break
            mostra_tabuleiro(TABELA)
            TABELA = jogada0(TABELA)
            aux, ganhador = verifica_ganhador(TABELA)
            if ganhador == 1:
                mostra_tabuleiro(TABELA)
                break
            
        if auxinicio == 1: ## Computador começa   
            mostra_tabuleiro(TABELA)
            TABELA = jogada0(TABELA)
            aux, ganhador = verifica_ganhador(TABELA)
            if ganhador == 1:
                mostra_tabuleiro(TABELA)
                break
            mostra_tabuleiro(TABELA)
            TABELA = jogadaX(TABELA)
            aux, ganhador = verifica_ganhador(TABELA)
            if ganhador == 1:
                mostra_tabuleiro(TABELA)
                break
                    
        jogadas = jogadas + 1
        if jogadas == 5:
            print("EMPATE, É O MÁXIMO QUE VAI CONSEGUIR!!! RSRSRS")
            break


    while 1:
        auxfim = input("Jogar novamente? \n 0 = não \n 1 = sim \n :")
        if auxfim == "0":
            fim = 0
            break
        elif auxfim == "1":
            ganhador = 0
            TABELA = np.zeros((3,3),int)
            jogadas = 0
            if auxinicio == 0:
                auxinicio = 1
            else:
                auxinicio = 0
            break
        else:
            print("Valor invalido!!!")

      








