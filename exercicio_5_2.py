cores= ['vermelho', 'Azul', 'verde']
for cor in cores:
    if cor.lower() == 'azul':
        print ("A cor "+ cor.lower()+" esta na lista de cores")

if (cores[0] != 'roxo'):
    print (cores[0]== 'roxo')

print ("Voce conhece as cores: "+ (str((cores[0]== 'vermelho') 
        and (cores[1].lower()== 'azul') and (cores[2] == 'verde'))))

valores= [50, 1, 150, 20, 200, 10]

if (valores[0] < valores[1]):
    print(str(valores[0])+" é menor que "+ str(valores[1]))
else:
    if (valores[0] >= valores[3]):
        print(str(valores[0])+" é maior ou igual a "+ str(valores[1]))

if (valores[3]< valores[4]) or (valores[4]>= valores[5]):
    print ("Dados inconsistentes")

for valor in valores:
    if (valor== 10):
        print ("O valor "+ str(valor) + " está na lista!")
        
resultado= 'False'
for valor in valores:
    if (valor == 50):
        resultado= 'True'
print (str(resultado))

if (resultado == 'False'):
    print ("O valor procurado não esta na lista")
else:
    print ("O valor procurado está na lista")
