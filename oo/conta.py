import abc
from excecoes import*


from historico import Historico

class Conta(abc.ABC): # abc.ABC torna a classe abstrata - não posso instanciar uma classe abstrata
    """As classes concretas devem sobrescrever o método atualiza"""
    
    _total_contas=0
    
    def __init__(self, numero, cliente, saldo, limite= 1000.00):
        print('\nInicializando a conta: {}'.format(numero))
        self.numero= numero
        self.titular= cliente
        self.saldo= saldo
        self.limite= limite
        self.historico= Historico() # Composicão - A classe Historico compõe a classe Conta
        Conta._total_contas += 1 # _total_contas  É atributo da classe e não do objeto
    
    def deposita(self, valor):
        if (valor< 0):
            raise ValueError('Você tentou depositar um valor negativo')
        else:
            self.saldo += valor
            self.historico.transacoes.append("deposito de {}".format(valor))
        
    def saca(self, valor):
        if (self.saldo < valor):
            raise ValueError('Você tentou depositar um valor negativo')
            return False
        else:
            self.saldo -= valor
            self.historico.transacoes.append("saque de {}".format(valor))
            return True
            
    def transfere_para(self, destino, valor):
        retirou= self.saca(valor)
        if (retirou):
            destino.deposita(valor)
            self.historico.transacoes.append("transferencia de {} para a conta {}".format(valor, destino.numero))
            return True
        else:
            return False

    def extrato(self):
        print('Numero: {} \nSaldo: {}\n'.format(self.numero, self.saldo))
        self.historico.transacoes.append("tirou extrato - saldo de   {}".format(self.saldo))
    
    @staticmethod  #decorador - inidica que o método é estático, ou seja, acessa um atributo da classe e não do objeto
    def get_total_contas():
        return Conta._total_contas
        
    @abc.abstractmethod
    def atualiza(self, taxa): # Este é um metodo abstrato
        self.saldo+= self.saldo * taxa
        return (self.saldo)
        
    def __str__(self): #Representa a classe como uma string
        return ('\nDados da Conta: \nTipo: {}\nNumero: {} \nTitular: {} \nSaldo: {} \nLimite: {}'.format(self.tipo, self.numero, 
            self.titular, self.saldo, self.limite))

class TributavelMixIn:
    def get_valorImposto(self):
         pass

class ContaCorrente(Conta, TributavelMixIn):
    tipo= 'ContaCorrente'
    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 2
        return (self.saldo)
        
    def deposita(self, valor):
        self.saldo += valor - 0.10
        
    def get_valorImposto(self):
        return self.saldo* 0.01
        
    def saca(self, valor):
        if (valor <0):
            raise ValueError('Você tentou sacar um valor negativo')
        if (self.saldo <valor):
            raise SaldoInsuficienteError('Saldo Insuficiente para o saque')
        self.saldo -= (valor+ 0.10)
        
class ContaPoupanca(Conta):
    tipo= 'ContaPoupança'
    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 3
        return (self.saldo)

class ContaInvestimento(Conta): #deve implementar os metodos abstratos da classe Conta
    tipo= 'contaInvestimento'
    def atualiza(self, taxa):
        self.saldo += self.saldo * taxa * 5
        return (self.saldo)
 
class SeguroDeVida(TributavelMixIn):
    def __init__(self, valor, titular, numero_apolice): 
        self._valor= valor
        self._titular= titular
        self._numero_apolice= numero_apolice
        
    def get_valorImposto(self):
        return 50.00+ self._valor* 0.05
    
if __name__== '__main__':
    #c= Conta('123-4', 'João', 1000.00) # Erro Conta é uma classe abstrata, não posso instanciar
    cc= ContaCorrente('123-5', 'José', 1000.00)
    cp= ContaPoupanca('123-6', 'Maria', 1000.00)
    
    #c.atualiza(0.01)
    cc.atualiza(0.01)
    cp.atualiza(0.01)
    
    #print(c.saldo)
    print(cc.saldo)
    print(cp.saldo)
    
    print(cc)
    print(cp)
    c1= ContaInvestimento('789', 'Vitor', 2000)
    print(c1)
    
    valor= 5000.00
    try:
        cc.saca(valor)
    except ValueError:
        print('O valor a ser sacado deve ser positivo')
    
    #help(Conta) #Exibe a documentação da classe conta
