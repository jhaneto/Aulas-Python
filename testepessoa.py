from pessoa import Pessoa
from pessoasexo import PessoaSexo

pessoa = PessoaSexo('Carlos', 12, 'M')
   
print(pessoa.getNome().split())
print(pessoa.getIdade())
print(pessoa.getSexo())

lista = list(range(1,4))
tupla = tuple(range(0,15))
lista.append([2,3,4,5])
print(lista)

print(tupla)

for i in lista:
    if isinstance(i, list):
        for n in i:
            if n == 5:
                print("a lista não conta o valor 5")


    else:
        if i == 5:
            print("A lista conta com o numero 5")



