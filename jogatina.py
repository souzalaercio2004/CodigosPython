import forca
import advinhacao

def escolher_Jogo():
    escolha=0
    while (escolha <=0 or escolha >2):
        print ('(1) - Jogar Forca')
        print ('(2) - Jogar Advinhação')
        escolha = int(input('Digite sua escolha: '))
    return escolha


# ********INICIO DO JOGO***********

escolha=  escolher_Jogo()   
if (escolha == 1):
    forca.jogar()
elif (escolha == 2):
    advinhacao.jogar()
