car= 'subaru'
if car == 'subaru':
    print("Is car == 'subaru'? I predict "+ str(car == 'subaru'))

if car == 'audi':
    print("\nIs car == 'audi'? I predict "+ str(car == 'subaru'))
    
sabores= ['acerola', 'coco', 'limão', 'uva', 'maracuja']

#for sabor in sabores:
#    if sabor== 'acerola':
#        print ("Tem sabor de acerola? " + str(sabor == 'acerola'))
#    else:           
#        if sabor == 'coco':
#            print ("Tem sabor coco? "+ str(sabor == 'coco'))
#        else:
#            if sabor== 'limão':
#                print ("Tem sabor limão? "+ str(sabor == 'limão'))
#            else:
#                if sabor == 'uva':
#                    print ("Tem sabor uva? "+ str(sabor == 'uva'))
#                else:
#                    print ("Tem sabor maracuja? "+ str(sabor == 'maracuja'))

falta_sabores= ['pequi', 'manga', 'abacate', 'laranja', 'jaca', 'acerola', 'coco', 'limão', 'uva', 'maracuja']

for falta_sabor in falta_sabores:
    if falta_sabor not in sabores:
        print ("Não temos sorvete no sabor "+ falta_sabor)
    else:
        print ("Temos sorvete no sabor "+ falta_sabor)
