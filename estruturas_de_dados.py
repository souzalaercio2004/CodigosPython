#Tuplas
aluno= 'Jose Carlos', 52, 'Virgem', 1.80 

print (type(aluno))
print('\n')

#aluno[0]= 'Antonio Carlos' # Geraria erro pois uma tupla é imutável
print (type(aluno[0]))
print (type(aluno[1]))
print (type(aluno[2]))
print (type(aluno[3]))
print('\n')

#Dicionario
curso= {'Nome':'Laércio', 'Idade':52, 'curso':'Ciencias da Computação'}

print(type(curso))
print('Nome: '+curso.get('Nome')+' Idade: '+str(curso.get('Idade'))+' Curso: '+curso.get('curso')+'\n')

