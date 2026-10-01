#!/usr/bin/env python3

# Exercício 7 - somar números pares e ímpares do conjunto com iterador for
p = [101,2,15,22,95,33,2,27,72,15,52]
p_ordenada = sorted(p) #ordenar em ordem numérica
print(p_ordenada)
soma_pares = 0
soma_impares = 0
for num in p:
    if num % 2 == 0: #identifica números pares
        soma_pares += num #números pares vão se somando até uma soma final 
    else: #restam os números ímpares
        soma_impares += num 
print ('Soma dos números pares: ',soma_pares, '\nSoma dos números ímpares: ', soma_impares)