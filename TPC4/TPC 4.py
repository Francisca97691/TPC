#!/usr/bin/env python
# coding: utf-8

# # TPC 4

# ## Frações

# ### Data de início: 2021-10-27

# ### Data do fim: 2021-11-03

# ### Supervisor: José Carlos Ramalho, https://www.di.uminho.pt/~jcr/

# ### Autor: Francisca Silva, a97691

# ### Resumo: Primeiramente, criou-se um menu, com as possíveis funções.Passando para as funções, em algumas optou-se por inserir as frações numa lista de tuplos, na forma [(numerador, denominador)]. Das funções definidas as fundamentais foram chamadas noutras de modo a facilitar as operações e simplificar o algoritmo. Por fim, foi criada uma função que consoante a opção do utilizador o leva à execução da operação desejada.

# In[ ]:


print("""MENU:
         (0) Sair
         (1) Criar fração
         (2) Simplificar fração
         (3) Somar
         (4) Subtrair
         (5) Multiplicar
         (6) Dividir
         (7) Gerar lista de n frações
         (8) Somar lista
         (9) Maior fração""")

def sair():
    print("That's all folks :)))")
    
    
def criarFracao():
    numerador = int(input("Insira o numerador: "))
    denominador = int(input("Insira o denominador: "))
    return (numerador, denominador)

def verFracao(f):
    print(str(f[0])+"/"+str(f[1]))
    
def mdc(a,b):
    if a < b:
        return mdc(b, a)
    elif a%b == 0:
        return b
    else: 
        return mdc(a, a%b)

def simplificarFracao(f):
    num, denom = f
    a = mdc(num, denom)
    return (num/a, denom/a)    

def somarFracao():
    f1 = criarFracao()
    f2 = criarFracao()
    n1, d1 = f1
    n2, d2 = f2
    return n1*d2 + n2*d1, d1*d2

def subtrairFracao():
    f1 = criarFracao()
    f2 = criarFracao()
    n1, d1 = f1
    n2, d2 = f2
    return n1*d2 - n2*d1, d1*d2

def multiplicarFracao():
    f1 = criarFracao()
    f2 = criarFracao()
    n1, d1 = f1
    n2, d2 = f2
    return n1*n2, d1*d2

def dividirFracao():
    f1 = criarFracao()
    f2 = criarFracao()
    n1, d1 = f1
    n2, d2 = f2
    return n1*d2, d1*n2

def gerarLista():
    lista = []
    listaDecimal = []
    n = int(input("Insira o comprimento da lista: "))
    i = 0
    while i < n:
        num = int(input("Insira o numerador: "))
        den = int(input("Insira o denominador: "))
        tuplo = (num, den)
        lista.append(tuplo)
        listaDecimal.append(num/den)
        i += 1
    return lista
    
L = gerarLista()

def somarLista(L):
    res = (0,1)
    for elem in L:
        f1 = res
        f2 = elem
        n1, d1 = f1
        n2, d2 = f2
        res = n1*d2 + n2*d1, d1*d2
    return res

def maiorLista(L):
    maior=-1000000000000000000000000
    listaDecimal=[]
    i=-1
    for elem in L:
        elem=elem[0]/elem[1]
        listaDecimal.append(elem)
    for elem in listaDecimal:
        if elem>maior:
            maior=elem
            i+=1
    print("A maior fração é", L[i])
    return maior
L1 = maiorLista(L)

def opcao():
    op = str(input("Insira um dos comandos do menu: "))
    while op != '0':
        if op == '1':
            f = criarFracao()
        elif op == '2':
            print(verFracao(simplificarFracao(f)))
        elif op == '3':
            f = somarFracao()
            print(verFracao(simplificarFracao(f)))
        elif op == '4':
            f = subtrairFracao()
            print(verFracao(simplificarFracao(f)))
        elif op == '5':
            f = multiplicarFracao()
            print(verFracao(simplificarFracao(f)))
        elif op == '6':
            f = dividirFracao()
            print(verFracao(simplificarFracao(f)))
        elif op == '7':
            gerarLista()
        elif op == '8':
            f = somarLista(L)
            print(verFracao(simplificarFracao(f)))
        elif op == '9':
            f = maiorLista(L)
            print(f)
        else:
            print("Este número não está nas alternativas, tente novamente :D.\n")
        op = str(input("Insira um dos comandos do menu: "))
    if op == '0':
        sair()
opcao()


# In[ ]:





# In[ ]:




