#Tratamento de excessões
from conta import ContaCorrente

def metodo1():
    print ('Início do método 1')
    
    metodo2()
    print('Fim do método1')
    
def metodo2():
    print('Início do método 2')
    cc= ContaCorrente('José', '123', 1000.00)
    
    for i in range(1,15):
        cc.deposita(i+1000.00)
        print(cc.saldo)
        if (i== 5):
            cc= none

    print('Fim do método 2')
        
#Execucao
if __name__== '__main__':
    print('Início do main')
    try:
        metodo1()
    except:
        print('erro')
        
    print('Fim do main')
    
