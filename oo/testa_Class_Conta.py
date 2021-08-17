# -*- coding: utf-8 -*-
# #testa_Class_Conta


from cliente import Cliente
from conta import Conta

#Parametros: (self, numero, cliente, saldo, limite)
novo_Cliente= Cliente('Marcelo', 'Oliveira', '111.111.111-11')
conta= Conta('123-4', novo_Cliente, 120.00, 1000)
conta.deposita(20.00)
conta.extrato()
conta.extrato()

conta.saca(15.00)
conta.extrato()

conta.saldo= 1000.00

if (conta.saca(800)):
    print('Consegui Sacar ')
    print ('Para o cliente {} {}.\n'.format(conta.titular.nome, conta.titular.sobrenome))
else:
    print('Nao consegui Sacar\n')

#print(conta.titular)
print('Saldo da conta= {}'.format(conta.saldo))
conta2= conta # Conta2 é uma referencia para conta
print('Saldo da conta2= {}'.format(conta2.saldo))

conta2.deposita(30)
print('Saldo da conta= {}'.format(conta.saldo))
print('Saldo da conta2= {}'.format(conta2.saldo))

# A funcao internaid(objeto) retorna o endereço em memoria do objeto
print(id(conta) == id(conta2)) 

novo_cliente3= Cliente('Antonio', 'Carlos de Oliveira', '111.131.151-13')
conta3= Conta('124-7', novo_cliente3, 120.00, 1500)
conta2.extrato()
if(conta2.transfere_para(conta3, 22.00)):
    print('Transferencia bem sucedida')
    print('para o cliente {} {}'.format(conta3.titular.nome, conta3.titular.sobrenome))
else:
    print('Falhou a transferencia, saldo insuficiente')

conta3.extrato()
print('Limite: {}'.format(conta3.limite))


#testando conta com historico
print('\ntestando conta com historico')

cliente1= Cliente('João', 'Oliveira', '111111111-11')
cliente2= Cliente('José', 'Azevedo', '222222222-22')
contax= Conta('153-4', cliente1, 1000.00)
contay= Conta('456-7', cliente2, 1000.00)

contax.deposita(100.00)
contax.saca(50)
contax.transfere_para(contay, 200.00)
contax.extrato()

contax.historico.imprime()

contay.historico.imprime()

print('Quantidade de Contas: {}'.format(contay.get_total_contas()))
