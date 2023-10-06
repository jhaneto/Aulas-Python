class Evento:
      def altera_evento_nome(self, novo_nome):
         print("Alterando nome")
         self.nome = novo_nome
        

ev = Evento()
ev.nome = "Aula de Python"
print("Aula de JavaScritp")        
ev.altera_nome_evento("Aula de Java")
print(ev.nome)