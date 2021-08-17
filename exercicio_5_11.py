numeros= list(range(1,10))
numeros_ordinais= []

for numero in numeros:
    if numero == 1:
        numeros_ordinais.append(str(numero)+ "st")
    elif numero == 2:
        numeros_ordinais.append(str(numero)+ "nd") 
    elif numero == 3:
        numeros_ordinais.append(str(numero)+ "rd")
    else:
        numeros_ordinais.append(str(numero)+ "th")
    
print (numeros_ordinais)

