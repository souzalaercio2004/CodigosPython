sabores= ['portuguesa', 'quatro queijos', 'marguerita']
friend_pizzas= sabores[:] # Faz um copia da lista de sabores
sabores.append('gorgonzola')
friend_pizzas.append('tomate seco')

print ("Minhas pizzas favoritas são: ")
for sabor in sabores:
	print(sabor.title())
	
print ("\nAs pizzas favoritas do meu amigo são: ")
for friend in friend_pizzas:
	print (friend.title())


