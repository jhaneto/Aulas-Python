from dominio import Usuario, Lance, Leilao, Avaliador

almeida = Usuario('Almeida')
sheila = Usuario('Sheila')

lance_almeida = Lance(almeida, 200.00)
lance_sheila = Lance(sheila, 100.00)

leilao = Leilao('Celular')

leilao.lances.append(lance_almeida)
leilao.lances.append(lance_sheila)


for lance in leilao.lances:
    print(f'O usuario {lance.usuario.nome} o deu o lance de {lance.valor}')

avaliador = Avaliador()
print(avaliador)
avaliador.avalia(leilao)

print(f'O menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')