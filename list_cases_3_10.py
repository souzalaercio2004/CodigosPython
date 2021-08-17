lista= []
lista.append('frango') # Insere elemento no fim da lista
lista.append('quiabo') # Insere elemento no fim da lista
print (lista)

lista[0]= lista[0]+" com "+lista[1] # faz concatenação de elementos da lista
del(lista[1])

print (lista)
lista.append('macarão') # Insere elemento no fim da lista
lista.append('linguiça') # Insere elemento no fim da lista
lista.append('salada') # Insere elemento no fim da lista

print (lista)
print (lista[0].title()) # Exibe o primeiro elemento com iniciais maiusculas
print (lista[0].lower()) # Exibe o primeiro elemento com as iniciais em minusculas
print (lista[0].upper()) # Exibe o primenro elemento com todas as letras maiusculas
print(lista[1])

print(sorted(lista))
print(sorted(lista, reverse= True)) #Exibe a lista na ordem inversa
print (lista)
lista.reverse()
print (lista)

removido= lista.pop() # Remove o elemento do final da lista
print("Removemos "+removido+ " da lista")
print (lista)

lista.insert(1, 'azeite') # Insere elemento na posição 1 da lista e desloca os demais
print (lista)

lista.sort()
print (lista)

removido= lista.pop(3) # Remove elemento da posição 3
print("Removemos "+ removido)

lista.append('pudim') #Insere elemento no fim da lista
print(lista)

lista.remove('azeite') # Remove o primeiro elemento de valor especificado  como parametro
print (lista)

del (lista[2])
lista.reverse()
print (lista)
print("A lista esta com tamanho "+str(len(lista)))  #Exibe o tamanho da lista
print (len(lista))
print (lista[-1]) #Exibe o ultimo elemento da lista
