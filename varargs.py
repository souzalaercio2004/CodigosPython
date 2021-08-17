#Varios argumentos
def soma(*varargs):
    total=0
    print(type(varargs)) # Uma tupla é imutável
    for valor in varargs:
        total +=valor
    print ('Soma= '+str(total)+'\n')
    
def funcionario(**args):
    for key in args:
       print ('Dia: '+args.get(key))
    print (args)
    print (args.keys())
    print (args.values())


soma (10, 20, 30) # Tupla
pessoa= {'1': 'Domingo', '2':'Segunda', '3':'Terça', '4':'Quarta'} #Dicionario
funcionario(**pessoa)

