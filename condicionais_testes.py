cor= 'Azul'
cor1= 'azul'

if (cor1 == cor.lower()):
    print ("as cores são semanticamente iguais")

if (cor1 != cor) and (cor1== cor.lower()):
    print ("As cores são semanticamente iguais mas estão com ortografias diferentes")

valor= 10
valor1= 150
valor2= 200
valor3= 10

print (valor == valor3)
print (valor < valor1)
print (valor2 > valor3)
print (valor1 <= valor2)
print (valor <= valor3)
print (valor3 >= valor2)

if (valor == valor3) and (valor1 < valor2):
    print ("Os valores do extremo são iguais e o segundo é menor que o terceiro")

if (valor3 < valor2) or (valor2 <= valor1):
    print ("Desigualdade satisfeita")

cores= ['azul', 'branco', 'verde']

if 'marron' in cores:
    print ("A cor desejada esta na lista de cores")
else:
    print ("Cor desconhecida")

if 'branco' in cores:
    print ("Cor já cadastrada")
