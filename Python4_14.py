#!/usr/bin/env python3

#Exercício bônus 1

from random import randrange

sequence = list("PROGRAMAÇÃO") #strings são imutáveis, diferente de listas, por isso é importante alterar a classe desse valor

for i in range(len(sequence)): #serão feitas 11 permutações na palavra 'PROGRAMAÇÃO', possibilitando um embaralhamento diferente a cada impressão
    A = randrange(len(sequence)) #as posições A e B escolhida pode ser entre qualquer elemento da lista
    B = randrange(len(sequence))

    sequence[A], sequence[B] = sequence[B], sequence[A] #essa permutação será realizada 11 vezes, cada vez trocando de lugar dois elementos da lista

print("".join(sequence)) #depois de embaralhada, a lista é impressa como uma string novamente, eliminando as aspas separadoras