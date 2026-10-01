#!/usr/bin/env python3
# Exercício 2
taxa = 'sapiens, erectus, neanderthalensis' #instrução 1 - Criar string
print('string original: ',taxa) #instrução 2 - imprimir a string
print('segundo elemento da string: ',taxa[1]) #instrução 3- imprimir taxa[1], o que resulta em o segundo 'caractere' e não no elemento 'erectus'
print('tipo do objeto taxa: ',type(taxa)) #instrução 4 - imprimir o tipo da variável taxa, que é uma string e não uma lista
split_taxa = taxa.split(', ') #instrução 5 - dividir a string em uma lista de strings
print('taxa como lista: ',split_taxa)
species = split_taxa #instrução 6 - criar uma lista de strings a partir da variável split_taxa
print('lista salva em ''species'': ',species) #instrução 7 - imprimir a lista de strings species
print('segundo elemento da lista: ',species[1]) #instrução 8 - imprimir species[1], agora sim vai ser impresso o elemento 'erectus'
print('tipo do objeto salvo em ''species'': ',type(species)) #instrução 9 - imprimir o tipo da variável species, que é uma lista
species_sorted = sorted(species) #instrução 10 - ordenar a lista species em ordem alfabética
print('lista em ordem alfabética: ',species_sorted) 
species_tamanho = sorted(species, key = len) #instrução 11 - ordenar a lista species pelo tamanho da string
print('lista em ordem de tamanho da palavra: ',species_tamanho) 
