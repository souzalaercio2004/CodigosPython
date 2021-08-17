#Calculo da Velocidade
def velocidade_media(distancia, tempo):
    if (tempo <= 0):
        print('Valor do tempo deve ser maior que zero')
        exit(1)
    return(distancia/tempo)


def soma(n1, n2):
    return(n1 + n2)
    
def subtracao(n1, n2):
    return(n1 - n2)
    
def multiplicacao(n1, n2):
    return(n1 * n2)
    
def divisao(n1, n2):
    if (n2 ==0):
        exit(1)
    return (n1/n2)

def potenciacao(base, expoente):
    return(base**expoente)

def fatorial(n):
    fat= 1
    for i in range(1, n+1, 1):
        fat*= i
    return (fat)
