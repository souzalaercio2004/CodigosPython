motorcycles= ['honda', 'yamaha', 'susuki']
print (motorcycles)
motorcycles[0]= 'ducati'  # troca o valor do primeiro elemento da lista
print (motorcycles)
motorcycles.append('kawasaki') # Insere um elemento no final da lista
print (motorcycles)
motorcycles= []
print(motorcycles)

motorcycles.append('kawasaki')
motorcycles.append('yamaha')
motorcycles.append('honda')
motorcycles.append('bugatti')

print(motorcycles);
motorcycles.insert(1, 'caloi') #insere um elemento na posição 1 da lista
print(motorcycles)

del motorcycles[2] # remove o elemento da posição 2 da lista
print (motorcycles)

popped_motorcycle= motorcycles.pop() #Remove um elemento no final da lista armazena-o em popped_motorcycle
print (popped_motorcycle) #Exibe item removido pela instrução anterior
print (motorcycles)

removida= motorcycles.pop(1)
print ("Acabamos de remover "+ removida)
print(motorcycles)

too_expensive= 'kawasaki'
motorcycles.remove(too_expensive) # Remove a primeira ocorrencia de too_expensive
print(motorcycles);
print ("\n A " +too_expensive.title() + " is too expensive for me.")
