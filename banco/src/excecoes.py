class RunTimeError(Exception):
    pass
    
class SaldoInsuficienteError(RunTimeError):
    """ Seu saldo é menor que o valor desejado"""
    pass
    
    def __init__(self, value):
        self.value= value
   
    def __str__(self):
        return repr(self.value)

