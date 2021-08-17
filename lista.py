lista= [12, -2, 4, 8, 29, 45, 78, 36, -17,2, 12, 8, 3, 3, -52]
pares= []
maximo= max(lista)
minimo= min(lista)
primeiro= lista[0]
contador= 0
media= 0.0
soma_negativos=0

tamanho= len(lista) # Tamanho da lista
for valor in lista:
    if ((valor % 2)==0):
        pares.append(valor)

# Conta a quantidade de valores iguais ao primeiro elemento
for valor in lista:
    if valor == lista[0]:
        contador+=1

# Calcula a média dos valores da lista
for valor in lista:
    media+=valor
media= media/tamanho

#Somatorio dos valores negativos
for valor in lista:
    if (valor < 0):
        soma_negativos+= valor
    
#Exibe os resultados na tela
print('Maximo= '+str(maximo))
print('Minimo= '+str(minimo))
print (pares)
print ('Número de ocorrências do primeiro elemento na lista: '+str(contador))
print ('Media: '+str(media))
print ('Soma dos valores negativos: '+str(soma_negativos))

#Retorna um Dicionario
def	calculadora(x,	y):
    return	{'soma':x+y,	'subtração':x-y,   'multiplicacao':x*y,   'divisao':x/y,   'potenciacao':x**y}
    
resultados	=	calculadora(10,	2)
for	key	in	resultados:
    print('{} : {}'.format(key,	resultados[key]))
