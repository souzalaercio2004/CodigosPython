from funcionario import Funcionario
import csv

arquivo= open('funcionarios.txt', 'r')
leitor= csv.reader(arquivo)

funcionarios= []


for linha in leitor:
    func= Funcionario(linha[0], linha[1], linha[2])
    funcionarios.append(func)
    
for f in funcionarios:
    print(f._salario)

arquivo.close()
