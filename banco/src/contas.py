#contas.py

from collections.abc import MutableSequence
from conta import *

""" Implementacao da classe abstrata Contas"""

class Contas(MutableSequence):
    _dados= []

    def __delitem__(self, posicao):
        
        del self._dados[posicao]
        
    def __getitem__(self, posicao):
        
        return self._dados[posicao]

    def __len__(self):
        
        return len(self._dados)
        
    def __setitem__(self, posicao, valor):
        if (isinstance(valor, Conta)):
            self._dados[posicao]= valor
        else:
            raise TypeError('O valor fornecido não é uma Conta')
        
    def insert(self, posicao, valor):
        if (isinstance(valor, Conta)):
            return self._dados.insert(posicao, valor)
        else:
            raise TypeError('O valor fornecido não é uma Conta')

if __name__ == '__main__':
    import csv
    contas= Contas()
    
    arquivo= open('contas.txt', 'r')
    leitor= csv.reader(arquivo)
    
    for linha in leitor:
        conta= ContaCorrente(linha[0], linha[1], float(linha[2]), float(linha[3]))
        contas.append(conta)
    arquivo.close()
    
    print('saldo - Imposto')
    for c in contas:
        print('{} - {}'.format(c.saldo, c.get_valorImposto()))
