from collections.abc import Container
from collections.abc import Sized
from collections.abc import Iterable
from collections.abc import MutableSequence
from funcionario import Funcionario

class Funcionarios(MutableSequence):
    _dados= []
    
    def __contains__(self, item):
        return self._dados.__contains__(self, item)
        
    def __len__(self):
        return len(self._dados)
        
    def __iter__(self):
        return self._dados.__iter__()
        
    def __setitem__(self, posicao, valor):
        if (isinstance(valor, Funcionario)):
            self._dados[posicao]= valor
        else:
            raise TypeError('Valor atribuido não é um funcionario')
        
    def __getitem__(self, posicao): #Garante que a classe é um container e iterable
        return self_dados[posicao]
        
    def __delitem__(self, posicao):
        del self._dados[posicao]
    
    def insert(self, posicao, valor):
        if (isinstance(valor, Funcionario)):
            return self._dados.insert(posicao, valor)
        else:
            raise TypeError('Valor atribuido não é um funcionario')
        
    
    
if __name__ == '__main__':

    funcionarios= Funcionarios()
    
