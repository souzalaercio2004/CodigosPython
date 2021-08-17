pratos= ('arroz', 'feijão', 'salada', 'bife', 'pudim') #Cria uma tupla

for prato in pratos:
	print (prato)
print("\n\n")
#pratos[0]= 'file' #TypeError: 'tuple' object does not support item assignment

#Aqui modificamos uma variavel - Isto esta correto
pratos= ('churrasco', 'vinagrete', 'salada', 'pão de alho', 'pudim') 
for prato in pratos:
	print (prato)                                                                    
