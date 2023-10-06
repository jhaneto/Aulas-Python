lista =  [2,4,5,6,1,6,7,8,9]
print(lista)
lista.extend([10, 15,16])
print(lista)

idades = [(idade+1) for idade in lista]
print(idades)

idade_maior = [idade+1 for idade in lista if idade > 6]
print(idade_maior)

lista = ["p", "y", "t", "h", "o", "n"]

for key, value in enumerate(["p", "y", "t", "h", "o", "n"]):
    print (key, value)
    
languages = ['Python', 'Java', 'JavaScript']

enumerate_languages = enumerate(languages)

# convert enumerate object to list
print(list(enumerate_languages))    