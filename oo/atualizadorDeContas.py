from conta import Conta
from conta import ContaCorrente
from conta import ContaPoupanca

class AtualizadorDeContas:
    def __init__(self, selic, saldoTotal=0):
        self._selic= selic
        self._saldoTotal= saldoTotal
        
    def roda(self, conta):
        print('Saldo da conta: {}'.format(conta.saldo))
        self._saldoTotal+= conta.atualiza(self._selic) 
        print ('Saldo final: {}\n'.format(self._saldoTotal))
        
if __name__== '__main__':
    #c= Conta('123-4', 'João', 1000.00) # A classe Conta e Abstrata
    cc= ContaCorrente('123-5', 'José', 1000.00)
    cp= ContaPoupanca('123-6', 'Maria', 1000.00)
    
    adc= AtualizadorDeContas(0.01)
    #adc.roda(c) # Não podemos criar instancia de classe abstrata
    adc.roda(cc)
    adc.roda(cp)
    
    print ('Saldo total: {}'.format(adc._saldoTotal))
    print (vars(adc))# mapeia as variaveis do objeto
