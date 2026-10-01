#!/usr/bin/env python3

# Exercício 13 - imprimir sequências com posição e comprimento delas
sequencias = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for sequencia in sequencias:
   print(sequencias.index(sequencia) + 1, len(sequencia), sequencia) #método index() retorna a posição, porém inicia-se no 0, portanto adicionar +1 é necessário para iniciar contagem no 1