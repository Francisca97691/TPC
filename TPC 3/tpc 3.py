#!/usr/bin/env python
# coding: utf-8

# # TPC 3
# 

# ## Bubble sort

# ### Data de início: 2021-10-20

# ### Data do fim: 2021-10-23

# ### Supervisor: José Carlos Ramalho, https://www.di.uminho.pt/~jcr/

# ### Autor: Francisca Silva, a97691

# ### Resumo:
# 
# #### Primeiramente, criou-se uma lista igual à introduzida pelo utilizador , para servir de termo de comparação.
# 
# #### Através de estruturas cíclicas realizou-se a comparação de dois elementos consecutivos. Caso o segundo seja maior que o primeiro avança-se uma posição , se o primeiro for maior procede-se à troca de posição, com recurso aos métodos de uma lista , nomeadamente *insert* e *pop*. De salientar que em ambas as opções é somado um ao contador i. 
# 
# #### No fim do primeiro ciclo de trocas verifica-se se a lista obtida é diferente da inicial. Se forem iguais então a lista encontra-se totalmente ordenada e o programa acaba, caso contrário inicia-se novamente o ciclo.
# 
# 

# 
# 

# In[ ]:


n=int(input("Introduza o número de elementos da lista:"))
l=[]
for j in range (n):
    elemento=int(input("introduza o elemento: "))
    l.append(elemento)
def bubble_sort(l):
    i = 0
    l1 = []
    for elem in l :
        l1.append(elem)
    while i < (len(l) - 1):
        if l[i] > l[i + 1]:
            l.insert(i, l[i + 1])
            l.pop(i+2)
            i += 1
        else:
            i += 1
    while l1 != l:
        i = 0
        l1 = []
        for elem in l :
            l1.append(elem)
        while i < (len(l) - 1):
            if l[i] > l[i + 1]:
                l.insert(i, l[i + 1])
                l.pop(i+2)
                i += 1
            else:
                i += 1
bubble_sort(l)
print(l)

