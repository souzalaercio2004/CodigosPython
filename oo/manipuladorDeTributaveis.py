class ManipuladorDeTributaveis:
    def calcula_impostos(self, lista_tributaveis):
        total= 0
        for t in lista_tributaveis:
            total+= t.get_valorImposto()
        
        return total
        
#Testando
if __name__ == '__main__':
    total= 0
    from conta import ContaCorrente, SeguroDeVida, TributavelMixIn
    
    cc1= ContaCorrente('123-4', 'João', 1000)
    cc2= ContaCorrente('124-4', 'Jose', 1000)
   
    seguro1= SeguroDeVida(100.00, 'José', '345-77')
    seguro2= SeguroDeVida(200.00, 'Maria', '237-98')
    
    lista_tributaveis= []
    lista_tributaveis.append(cc1)
    lista_tributaveis.append(cc2)
    
    lista_tributaveis.append(seguro1)
    lista_tributaveis.append(seguro2)
    
    manipulador= ManipuladorDeTributaveis()
    total= manipulador.calcula_impostos(lista_tributaveis)
    
    print(total)
    
