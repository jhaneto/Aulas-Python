from pessoa import Pessoa
   
class PessoaSexo(Pessoa):  
      def __init__(self,nome, idade, sexo):
             super().__init__(nome, idade)
             self.sexo = sexo
             
             
      def getSexo(self):
        return self.sexo
    
      def setSexo(self, sexo):
        self.sexo = sexo
        
        