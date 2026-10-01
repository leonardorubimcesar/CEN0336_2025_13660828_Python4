#!/usr/bin/env python3

# Exercício 5 - calcular o fatorial de 1000

fatorial = 1
contagem = 1
while contagem <= 1000:
   fatorial = contagem * fatorial
   contagem+=1 #à medida que contagem aumenta de 1 até 1000, fatorial vai sendo calculado, resultando em fatorial de 1000
print(fatorial)