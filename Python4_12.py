#!/usr/bin/env python3

# Exercício 12 - usar compreensão de lista para gerar lista de tuplas
sequencias = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
tuplas = [(len(seq), seq) for seq in sequencias] #lista de tuplas é formada iterando cada elemento com seu comprimento
print(tuplas)