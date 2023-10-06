class Cliente:
    
    def __init__(self, nome):
        self.__nome= nome
        
    @property   
    def nome(self):
        print("Executando o metodo Property")
        return self.__nome.title()
    
    @nome.setter
    def nome(self, nome):
        print("Executando o metodo setter nome")
        self.__nome = nome 
    
    
    
    
              