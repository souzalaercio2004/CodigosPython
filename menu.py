import forca
import advinhacao

print('*********************************')
print('**********MENU	DE	JOGOS**********')
print('*********************************')
print("1. Adivinhação")
print("2. Forca")
escolha	=	int(input("Qual jogo quer jogar? Digite	o número: "))

if escolha	==	1:
    advinhacao.jogar()
elif escolha	==	2:
    forca.jogar()

