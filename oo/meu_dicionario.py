from collections import UserDict

class Pins(UserDict):
    
    def __contains__(self, key):
        return str(key) in self.keys()
        
    def __setitem__ (self, key, value): # garante que a chave sempre sera uma string - classe sobrescrita
        self.data[str(key)]= valeu
    
    if __name__=='__main__':
            pins= Pins(one=1)
            print(pins)
            pin[3]= 1
            lista= [1, 2, 3]
            pins[lista]= 2
            print(pins)
