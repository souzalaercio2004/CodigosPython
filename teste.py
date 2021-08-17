import funcoes
import advinhacao


vel= funcoes.velocidade_media(100, 10)
print ('Velocidade Media: {:.2f}'.format(vel)+' m/s')

print (funcoes.soma(10,20))
print (funcoes.multiplicacao(17, 13))
print (funcoes.subtracao(158, 16))
print (funcoes.divisao(1024,128))
print (funcoes.potenciacao(2,10))
print (funcoes.fatorial(6))

advinhacao.jogar()


