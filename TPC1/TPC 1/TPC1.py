# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 10:54:10 2021

@author: 35191
"""
import random 

def jogo():
     jogador=input(" Quer ser o jogador 1 ou 2?")
     if jogador=="1": #certo menos numero negativo fosforos
          i = 21
          while i > 0 :
           a = int(input("Quantos fósforos quer retirar? ")) 
           if a < 1 or a > 5 :
               print ("Não é possível retirar essa quantidade de fósforos ")
               return
           else:
               i = i - a
               print ("Após a sua jogada sobraram ", i, " fósforos :) ")
               b = 5 - a     # o b é o numero de fosforos que vao ser retirados pelo computador
               if i>0:
                  i = i - b  
                  print ("Sobraram ", i ," fósforos após a jogada do computador :) ")
               else:
                  print("Perdeu :( ")
     elif jogador=="2":
          i=21
          while i>1:
              b=random.randint(1, 4)
              i=i-b
              print ("Após a jogada do computador sobraram ", i, " fósforos :) ")
              a=int(input("Quantos fósforos quer retirar? ")) 
              if a < 1 or a > 4 :
                 print ("Não é possível retirar essa quantidade de fósforos ")
                 return
              else: 
                 i = (i-a)
                 print ("Restam " + str(i) + " fósforos.")
                 if i == 1 :
                    print ("Ganhou o jogo :)")
                 elif i <= 5 and i > 1:
                     b = i-1
                     i = i-b 
                     print ("O adversário jogou: " + str(b) + "\n" + "Restam:" + str(i) + " fósforos." + "\n" + "O jogador 1 ganhou!")
                 elif a+b < 5 :
                     b = 5-(a+b)
                     i = (i-b)
                     print ("O adversario jogou: " + str(b) + "\n" + "Restam:" + str(i) + " fósforos.")
                     if i == 1 :
                        print ("O jogador 1 ganhou!")
     else:
         print ("Introduza corretamente se quer ser o jogador 1 ou 2, digitando 1 ou 2")
              
         
             
             
                     
     
         
     
jogo()
    
