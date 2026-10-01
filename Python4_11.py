#!/usr/bin/env python3

# Exercício 11 - criar lista, iterar e imprimir comprimentos
sequencias = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
print('----parte 1: imprimir cada elemento----')
for sequencia in sequencias:
    print(sequencia)
print('----parte 2: imprimir cada elemento com comprimento----')
for sequencia in sequencias:
    print(len(sequencia), sequencia) #len() retorna número de elementos em cada string
