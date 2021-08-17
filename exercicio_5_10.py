curent_users= ['vania', 'adelson', 'bete', 'denecy', 'lucimar']
new_users=['andressa', 'laercio', 'Denecy', 'ADELSON', 'lula']

for curent_user in curent_users :
    i= 0
    igual= False
    for new_user in new_users:
        
        if (new_user.upper() == curent_user.upper()):
            igual= True
            new_users[i]= input ('Forneça um novo nome: ').lower()
        i = i+1
    if (igual== False):
        print('Nome disponível!')     
        
    
print(curent_users)
print (new_users)
