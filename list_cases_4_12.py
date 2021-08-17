my_foods= ['pizza', 'falafel', 'carrot cake']
friend_foods= my_foods[:]

print("\nMy favorite foods are: ")
for my_food in my_foods:
	print (my_food)

print("\nMy friend's favorite foods are: ")
for friend_food in friend_foods:
	print (friend_food)

my_foods.append('cannoli')
friend_foods.append('ice crean')

print("\nMy favorite foods are: ")
for my_food in my_foods:
	print (my_food)

print("\nMy friend's favorite foods are: ")
for friend_food in friend_foods:
	print (friend_food)
