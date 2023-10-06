class Programa:
    def __init__(self, nome, ano):
        self._nome = nome
        self._ano = ano
        self._likes = 0
        
    @property    
    def nome(self):
        return self._nome.title()
    @nome.setter    
    def nome(self, nome):
        self._nome = nome
     
    @property
    def ano(self):
        print("@property ano")
        return self._ano
    @ano.setter
    def ano(self, ano):
        print("Setter ano")
        self.__ano = ano
        
    @property
    def likes(self):     
        return self._likes
    
    
    def dar_likes(self):
        self._likes=1
        print(self._likes)
        self._likes +=1
    
    def imprime(self):
        print(f'{self._nome} - {self._ano} - {self._likes} Likes')    
        
      
        
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao
        
    @property
    def duracao(self):
        return self._duracao
    @duracao.setter
    def duracao(self, duracao):
        self._duracao = duracao
        
    def imprime(self):
        print(f'{self._nome} - {self._ano} - {self._duracao} - {self._likes} Likes') 

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
       super().__init__(nome, ano)
       self._temporadas = temporadas
        
    @property
    def temporadas(self):
        return self._temporadas
    
    @temporadas.setter
    def temporadas(self, temporadas):
        self._temporadas = temporadas
     
    def imprime(self):
        print(f'{self._nome} - {self._ano} - {self._temporadas} - {self._likes} Likes') 

 
# class Playlist(list):
#      def __init__(self, nome, programas):
#          self.nome = nome
#          super().__init__(programas)
#
class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return  self._programas[item]

    @property
    def listagem(self):
        return self._programas
    
    def __len__(self):
       return len(self._programas) 
    
    @property
    def tamanho(self):  
        return len(self._programas)
    
