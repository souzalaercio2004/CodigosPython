from container import Funcionarios
from funcionario import Funcionario
import csv # Metodos para processar arquivo em formato csv

""" Testando o uso do container de Funcionarios"""

arquivo= open('funcionarios.txt', 'r')
leitor= csv.reader(arquivo)

funcionarios= Funcionarios() # Container de Funcionarios

for linha in leitor:
    func= Funcionario(linha[0], linha[1], float(linha[2])) # Objeto da Classe Funcionario
    funcionarios.append(func)# Inserindo o objeto no Container de Funcionarios
    
for f in funcionarios:
    
    print('{} - {}'.format(f._salario, f.get_bonificacao())) # Exibe o salario de um funcionario
    
arquivo.close()

print('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')

