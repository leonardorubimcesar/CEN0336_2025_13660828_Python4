#!/usr/bin/env python3

# Exercício 6 - imprimir números pares de uma lista iterando com loop for
p = [101,2,15,22,95,33,2,27,72,15,52]
for num in p: #for é usado quando há um conjunto fechado, já o while pode ser usado em conjuntos indefinidos
    if num % 2 == 0: #operador % é utilizado para identificar números divisíveis por algum número. No caso do '2', identifica-se os números pares, como no caso do exercício
        print(num)