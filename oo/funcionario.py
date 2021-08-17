class Funcionario:
    def __init__(self, nome, cpf, salario):
        self._nome= nome
        self._cpf= cpf
        self._salario= salario
    
    def get_bonificacao(self):
        return (self._salario* 0.10)
        
class Gerente(Funcionario): #Gerente herda de Funcionario
    def __init__(self, nome, cpf, salario, senha, qtd_gerenciados): # Método Sobrescrito
        super().__init__(nome, cpf, salario) #Chama o construtor da Super Classe
        self._senha= senha
        self._qtd_gerenciados= qtd_gerenciados
        
    def autentica(self, senha):
        if (self._senha == senha):
            print ('acesso permitido')
            return True
        else:
            print ('acesso negado')
            return False
            
    def get_bonificacao(self): # Sobrescrita do metodo
        return (super().get_bonificacao()+1000) # Usa o método da super classe 
        
class Diretor(Funcionario):
    def autentica(self, senha):
        if (self._senha == senha):
            print ('acesso permitido ao Diretor')
            return True
        else:
            print ('acesso negado ao Diretor')
            return False
            

class ControleDeBonificacoes:
    
    def __init__(self, total_bonificacoes=0):
        self._total_bonificacoes= total_bonificacoes
    
    def registra(self, obj):
        if(hasattr(obj, 'get_bonificacao')):
            try:
                self._total_bonificacoes+= obj.get_bonificacao()
            except Attribute_Error as e:
                print(e)
        else:
            print('Instancia de {} não implementa o método get_bonificacao()'.format(self.__class__.name))
  
class SistemaInterno:
    def login(self, funcionario):
        if (hasattr(obj, 'autentica')):
            funcionario.autentica()
        else:
            print('Você não possue acesso ao sistema')  
    
    @property
    def total_bonificacoes(self):
        return self._total_bonificacoes
    
#Gerente sobrescreve o método get_bonificação de Funcionário
gerente= Gerente('José ', '111123222-55', 5000, '1234', 0)          
print(gerente.get_bonificacao())
print(vars(gerente))

if ('name==__main__'):
    funcionario= Funcionario('Maria Ambrosina', '456124665-78', 2000.00)
    
    print ('bonificação funcionario: {}'.format(funcionario.get_bonificacao()))
    
    gerente= Gerente('José das Graças', '222333444-55', 5000.00, '1235', 0)
    print ('bonificação gerente: {}'.format(gerente.get_bonificacao()))

    controle= ControleDeBonificacoes()
    controle.registra(funcionario)
    controle.registra(gerente)
    print ('total: {}'.format(controle._total_bonificacoes))
    
