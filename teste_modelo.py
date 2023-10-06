from modelo import Programa, Filme, Serie, Playlist


gladiador = Filme("Gladiador", 2007, "3 horas")
frends = Serie("Frends", 2010, 4)
talves = Serie("Talvez", 2011, 5)
hferro = Filme("Homem de Ferro", 2010, "4 horas")
print(f'Nome do Filme: {gladiador._nome} - Ano : {gladiador._ano} - Duração : {gladiador._duracao} - Likes : {gladiador._likes}')
print(f'Nome do Serie: {frends._nome} - Ano : {frends._ano} - Duração : {frends._temporadas} - Likes : {gladiador._likes}')


print(f'Nome do gladiador: {gladiador._nome} - Ano : {gladiador._ano} - Duração : {gladiador._duracao} - Likes : {gladiador._likes}')
print(f'Nome do Serie: {frends._nome} - Ano : {frends._ano} - Duração : {frends._temporadas} - Likes : {gladiador._likes}')

gladiador.dar_likes()
frends.dar_likes()
talves.dar_likes()
hferro.dar_likes()

print(gladiador._likes)
print(frends._likes)

filme_serie = [gladiador, frends, talves, hferro]
playlist_assistidos = Playlist('Fim de semana', filme_serie)
print(playlist_assistidos)
# for programa in playlist_assistidos:
#     print(programa.nome)
#     print(programa)

print(f'Sim ou Não {gladiador in playlist_assistidos}')
