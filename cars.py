cars= ['bmw', 'audi', 'toyota', 'subaru']
print (sorted(cars)) # Lista temporariamente ordenada em ordem crescente

# Lista temporariamente ordenada em ordem decrescente
print (sorted(cars, reverse= True)) 
print (cars)# Lista Original
cars.reverse() # Inverte a ordem dos elementos na lista
print (cars)

cars.sort() # Ordena a lista em ordem crescente
print(cars)


cars.sort(reverse= True) # Ordena a lista em ordem decrescente
print(cars)

print("A lista tem tamanho= "+str(len(cars))+"\n")

#usando if
for car in cars:
    if car == 'bmw':
        print (car.upper())# Exibe a string com todas as letras maiusculas
    else:
        print (car.title()) #Exibe a string com a  primeira letra maiuscula
        
car= 'Audi'
print(car== 'audi')

# lower retorna a string com todas as letras minusculas
print (car.lower() == 'audi')
print (car)
