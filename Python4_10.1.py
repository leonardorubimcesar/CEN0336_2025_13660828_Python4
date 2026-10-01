#!/usr/bin/env python3

# Exercício 10 - imprimir numeros cujos valores de início e fim são dados pela linha de comando
import sys
count = int(sys.argv[1]) #para isso, usaremos sys.argv[]
while count < 100: #o valor de count poderia ser outro, visto que nosso objetivo é imprimir de 3 a 10
    print(count)
    count+=1 
    if count > int(sys.argv[2]): #se count for maior que número de fim, então break
        break