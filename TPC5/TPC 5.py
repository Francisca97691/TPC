#!/usr/bin/env python
# coding: utf-8

# # TPC 5

# ## Polinómios

# #### Data de início: 2021-11-11

# #### Data do fim: 2021-11-14

# #### Supervisor: José Carlos Ramalho, https://www.di.uminho.pt/~jcr/

# #### Autor: Francisca Silva, a97691

# #### Resumo: Neste trabalho percebeu-se que as funções desenvolvidas com os polinómios têm 2 dimensões, optando-se assim por fazer uma lista de tuplos, tendo os tuplos a forma (coeficiente,expoente).Primeiramente, criou-se um menu, com as possíveis funções.Das funções definidas as fundamentais foram chamadas noutras de modo a facilitar as operações e simplificar o algoritmo. Por fim, foi criada uma função que consoante a opção do utilizador o leva à execução da operação desejada. 

# In[ ]:


print("""MENU:
         (1) criar polinómio
         (2) calcular polinómio
         (3) calcular tabela
         (4) Simplificar polinómio
         (5) calcular a derivada de um polinómio
         (0)sair""")

def sair():
    print("That's all folks :)))")
    
n = int(input("Insira o comprimento do seu polinómio: ")) 
def criarPolinomio(n):
    pol = []
    i = 0
    while i < n:
        coeficiente= int(input("Insira o coeficiente do termo : "))
        expoente = int(input("Insira o expoento do termo : "))
        t = (coeficiente, expoente)
        pol.append(t)
        i += 1
    return pol

def verTermo(t):
    c, e = t
    return str(c)+'x^'+str(e)


def verPolinomio(p):
    res=" "
    for t in p:
        if res==" ":
            res=verTermo(t)
        else:
            res=res+"+"+verTermo(t)
    print (res)
    
    
def calcularPolinomio(p,x):
    x=int(input("Insira o valor de x: "))
    res=0
    for (c, e) in p:
        res=(res+c)*x**e
    return res



def simplificarPolinomio(poli):
    pos = 1 #segundo elemento do tuplo
    poli_length = len(poli)
    for i in range(0, poli_length):
        for j in range(0, poli_length-i-1):  
            if (poli[j][pos] > poli[j + 1][pos]):  
                temp = poli [j]  
                poli[j]= poli[j + 1]  
                poli[j + 1]= temp  
    return poli

    
def calcularTabela(p, nlinhas):
    x=int(input("Insira o valor de x: "))
    for i in range(nlinhas+1):
        print(str(i)+"::"+ str(calcularPolinomio(p,i)))
        
        
          
def derivarPolinomio(p):
    res = []
    for (c,e) in p:
        if e > 1:
            res.append((c*e, e-1))
    return res


def opcao():
    op = str(input("Insira um dos comandos do menu: "))
    while op != '0':
        if op == '1':
            polinomio = criarPolinomio(n)
            verPolinomio(polinomio)
        elif op == '2':
            x = int(input("Insira o valor de X: "))
            calcularPolinomio(polinomio, x)
        elif op == '3':
            numeroLinhas = int(input("Insira o numero de Linhas: "))
            calcularTabela(polinomio, numeroLinhas)
        elif op == '4':
            polinomio = criarPolinomio(n)
            simp=simplificarPolinomio(polinomio)
            verPolinomio(simp)
        elif op == '5':
            novoPolinomio = derivarPolinomio(polinomio)
            verPolinomio(novoPolinomio)
        else:
            print("Este nÃºmero nÃ£o estÃ¡ nas alternativas, tente novamente :D.\n")
        op = str(input("Insira um dos comandos do menu: "))
    if op == '0':
        sair()
opcao()
    

