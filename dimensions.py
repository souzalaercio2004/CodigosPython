dimensions= (200,50) #Cria uma tupla
print(dimensions[0])
print (dimensions[1])

#dimensions[0]= 250 #TypeError: 'tuple' object does not support item assignment
for dimension in dimensions:
	print(dimension)
	
#Sobrescrevendo uma tupla
dimensions= (400, 100) # Sobrescrever uma variável é uma operação valida
print ("\nModifield dimensions: ")
for dimension in dimensions:
	print(dimension)
