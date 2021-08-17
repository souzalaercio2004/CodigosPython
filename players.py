players= ['charles', 'matina', 'michael', 'florence', 'eli']
print (players[1:4]) # Exibe ['matina', 'michael', 'florence']
print ("Here are the first three players on my team: ")
print (players[:3]) # Exibe os tre primeiros elementos da lista a saber ['charles', 'matina', 'michael']

print (players[-3:]) #Exibe os tres elementos do final da lista a saber ['matina', 'michael', 'florence']
selecionados= players[:] # Cria uma copia da lista de players
print (selecionados)
