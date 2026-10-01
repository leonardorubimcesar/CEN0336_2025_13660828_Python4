#!/usr/bin/env python3

#Exercício 10 parte 2 - imprimir apenas ímpares
import sys
count = int(sys.argv[1])
while count < 100:
    if count % 2 != 0: #para imprimir apenas número ímpares
        print(count)
    count+=1
    if count > int(sys.argv[2]):
        break