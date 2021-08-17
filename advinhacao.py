import random

def start_advinhacao():
    print('********************************')
    print('Bem vindo ao jogo de adivinhação')
    print('********************************')
    print('\n')

def get_Numero():
    return(random.randrange(1,101))

def nivel_Difuculdade():
    valor=0
    while (valor<= 0 or valor >=3):
        print('Eu pensei em um número entre 1 e 100. Tente adivinha-lo!')
        print('Quer tentar em qual nível de dificuldade?')
        print('(1) Fácil  (2) Médio  (3) Difícil')
        valor = int(input("Defina seu nível: "))
        if (valor<= 0 or valor > 3):
            print('Escolha Invalida!')
        return valor
    
def numero_De_Tentativas(nivel):
    
    if(nivel == 1):
        tentativas = 20
    elif(nivel == 2):
        tentativas = 10
    else:
        tentativas = 5
    return (tentativas)

def processar_Palpite(rodada, total_tentativas, numero_secreto, pontos):
    print('Tentativa {} de {}'.format(rodada, total_tentativas))
    chute= 0
    while (chute <=0 or chute > 100):
        chute = int(input('Digite seu número: '))
    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print('Parabéns! Você acertou e fez {} pontos'.format(pontos))
        exit()
    else:
        if(menor):
            print('Lamento, você errou! Seu chute foi menor que o número secreto')
        elif(maior):
            print('Lamento, você errou! Seu chute foi maior que o número secreto')
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
    return pontos
    
def jogar():
    start_advinhacao()
    numero_secreto = get_Numero()
    pontos = 1000
    #acertou= False
    nivel = nivel_Difuculdade()
    total_tentativas = numero_De_Tentativas(nivel)
   
    for rodada in range(1,total_tentativas + 1):
        pontos= processar_Palpite(rodada, total_tentativas, numero_secreto, pontos)
    print ('\nO número secreto é: {}'.format(numero_secreto))        
    print('FIM DO JOGO')
