my_foods= ['pizza', 'falafel', 'carrot cake']
friend_foods= my_foods[:]

print("my favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print (friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice crean')

print("my favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print (friend_foods)

print("Os três primeiros itens da lista são: ")
print(my_foods[:3])

print("Os três itens do meio da lista são: ")
print(my_foods[1:4])

print("Os três ultimos itens da lista são: ")
print(my_foods[-3:])
