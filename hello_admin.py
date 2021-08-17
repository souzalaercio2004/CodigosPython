users= ['Arlindo', 'Letícia', 'admin',  'Lucas', 'Vivian']
if len(users) == 0:
    print ('Precisamos encontar alguns usuários')
else:
    for user in users:
        if user== 'admin':
            print ('Olá admin, gostaria de ver um relatório de status?')
        else:
            print('Olá ' + user+ ' obrigado por fazer login novamente.')
