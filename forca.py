import random
import os
#from PIL import Image, ImageFilter

def mensagem_Abertura():
    print ('**************************************')
    print ('***   Bem vindo ao jogo da Forca!  ***')
    print ('**************************************')
    print ('**************************************')


def carrega_Palavra_Secreta():
    arquivo= open('palavras.txt', 'r')
    palavras= []
    for linha in arquivo:
        linha= linha.strip()
        palavras.append(linha)
    
    arquivo.close()
    numero= random.randrange(0,	len(palavras))
    
    palavra_Secreta= palavras[numero].upper()
    
    return(palavra_Secreta)
    

def inicializa_Letras_Acertadas(palavra):
    return(['_' for letra in palavra])

def pede_Chute():
    chute= input ('Qual é a letra? ')
    chute= chute.strip().upper()
    return (chute)

def marca_chute_correto(chute, letras_Acertadas, palavra_Secreta):
    posicao= 0
    for letra in palavra_Secreta:
        letra.strip().upper()
        if (chute== letra):
            letras_Acertadas[posicao]= letra
            
        posicao= posicao + 1
    return letras_Acertadas
    
def voce_Ganhou(palavra):
    print('Parabéns, você ganhou!')
    print('A palavra era {}'.format(palavra))
    print('\n')
    print("       ___________        ")
    print("      '._==_==_=_.'       ")
    print("       .-\\:       /-.  ")
    print("       |(|:.        |)| ")
    print("       '-|:.        |-' ")
    print("         \\::.     /    ")
    print("          '::. .'         ")
    print("            ) (           ")
    print("          _.' '._         ")
    print("         '-------'        ")
    
    #im = Image.open("trofeu.jpg", "r")
    #Display image
    #im.show()

def voce_Perdeu(palavra):
    print('Puxa, você foi enforcado!')
    print('A palavra era {}\n'.format(palavra))
    print("      _______________")
    print("     /               \ ")
    print("    /                 \ ")
    print("  //                   \/\ ")
    print("\|       XXXXXXXX      | /")
    print(" |       XXXXXXXX      |/")
    print(" |        XXXXXX       |")
    print(" |                     |")
    print(" \__        XXX      __/")
    print("   |\       XXX     /|")
    print("   ||               ||")
    print("   |I  I  I  I  I  I|")
    print("   |I  I  I  I  I  I|")
    print("   \_             _/")
    print("     \_         _/")
    print("       \_______/")

def jogar():
    mensagem_Abertura()
    palavra_Secreta= carrega_Palavra_Secreta()
    letras_Acertadas= inicializa_Letras_Acertadas(palavra_Secreta)
    acertou= False
    enforcou= False
    erros= 0

    while (not acertou and not enforcou):
        chute= pede_Chute()
        
        if chute in palavra_Secreta:
            letras_Acertadas= marca_chute_correto(chute, letras_Acertadas, palavra_Secreta)
        else:
            erros += 1
            
        enforcou= erros== 7
        acertou= '_'not in letras_Acertadas
        print(letras_Acertadas)
        
    if acertou:
        voce_Ganhou(palavra_Secreta)
    else:
        voce_Perdeu(palavra_Secreta)
    
    print (30*'#')
    print ('Fim do Jogo')
