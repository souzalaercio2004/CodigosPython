#Função para gerar uma nova conta #
def cria_Conta(numero, titular, saldo, limite):
    conta={'numero':numero, 'titular':titular, 'saldo':saldo, 'limite':limite}
    return conta
    
#Função para incremetar saldo adicionando um valor """
def deposita(conta, valor):
    conta['saldo'] += valor

#Atualiza o saldo da conta decrementando o valor # 
def saca(conta, valor):
    conta['saldo'] -= valor

#Exibe o numero da conta e seu saldo
def extrato(conta):
    print ('numero: {}\nsaldo: {}\n'.format(conta['numero'], conta['saldo']))


#Execucao
conta_nova= cria_Conta('123-7', 'João', 500.00, 1000.00)
deposita(conta_nova, 50.00)
extrato(conta_nova)


saca(conta_nova, 20.00)
extrato(conta_nova)

