#Exercício 3
#método 1
>>> my_list = ['a', 'bb', 'ccc']  #criar lista
>>> list_copy = my_list #fazer cópia utilizando '='
>>> print(my_list) #imprimir my_lista
['a', 'bb', 'ccc']
>>> list_copy.append('dddd') #adicionar elemento à cópia
>>> print(my_list) #imprimir my_list novamente
['a', 'bb', 'ccc', 'dddd'] #my_list também foi alterada com alteração em list_copy

#método 2
>>> my_list2 = ['a', 'bb', 'ccc'] #criar lista
>>> list_copy2 = my_list2.copy() #criar cópia com método copy()
>>> print(my_list2) #imprimir my_list2
['a', 'bb', 'ccc'] 
>>> list_copy2.append('dddd') #adicionar elemento à cópia
>>> print(my_list2) #imprimir my_list2 novamente
['a', 'bb', 'ccc'] #utilizar o método copy() impede que my_list2 seja alterada, sendo alterada apenas list_copy2