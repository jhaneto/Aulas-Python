import random

baralho = [1,2,3,4,5,6,7,8,9,10,10,10]
tracinhofofo = ('-=')*20

print(f"{tracinhofofo}\n        BEM-VINDO(A) AO JOGO 21!\n{tracinhofofo}")

p1 = int(input("\nDIGITE: \n[1] PARA JOGAR\n[2] PARA SAIR\n>> "))

#Além da decisão de continuar...
#Aqui é uma variavel para receber todos os valores que o random.choice() escolhe.
p2 = total = x = 0
p3 = []

if p1 == "1":
    print("\nINICIANDO...")
elif p1 == "2":
    print("\nSAINDO...\nAté a Proxíma!")

while p2 != "N":
    #Aqui, cada vez que a pessoa continua, o X se torna SOMENTE um valor aleatorio do baralho
    x = random.choice(baralho)

    #O total soma o valor anterior mais o X escolhido na rodada
    total += x
    p3.append(x)
    
    
    print(f'Seu Valor Atual das Cartas é : {p3} o total {total}')
    #O jogo:
    print("\nSua carta é", x)
    p2 = str(input("Você quer mais cartas?\n>> ").upper()) #O .upper() joga o "N" e o "n(minusculo)" == N

    #Se ele não parar antes e o total for MAIOR que 21:
    if total > 21:
        print(f'\nVocê PERDEU!\nAs soma das cartas escolhidas foi {total} e PASSOU de 21!')
        break

    #Se ele não quiser continuar, e parar ANTES do resultado der 21:
    if p2 == 'N':
        print(f'\nPARABÉNS!\n As soma das cartas escolhidas foi {total} e deu menos que 21!')
        break