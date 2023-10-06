import io
import random

# with open('C:/Users/win10/Desktop/python alura/palavra.txt', 'w') as f:
#     f.write('Banana\n')
#      arquivo = open('C:/Users/win10/Desktop/python alura/palavra.txt', 'a')
#      arquivo.write("banana\n")
#      arquivo.write("manga\n")
#      arquivo.write("pera\n")
#      arquivo.write("laranja\n")
#      arquivo.write("melancia\n") 
#      arquivo.close()
def mostra_print_inicial():
     tracinho = ('-=')*30
     espaco = (' ')*4
     print(f"{tracinho}")
     print(f"{espaco}*************Bem Vindo ao Jogo da Forca***************{espaco}")
     print(f"{tracinho}")

def carrega_palavra_secreta():
    arquivo = open('C:/Users/win10/Desktop/python alura/palavra.txt', 'r')
    palavras = []
     
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
          
    arquivo.close()
    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    
    return palavra_secreta
def inicializa_letras_acertada(palavra):
     return ["_" for letra in palavra]

def jogar():
    
     mostra_print_inicial()
     palavra_secreta = carrega_palavra_secreta()

     letras_acertadas = inicializa_letras_acertada(palavra_secreta)
    
     print(letras_acertadas)
         
     enforcou = False
     acertou  = False
     error    = 0
     
     while(not enforcou and not acertou):
         
         chute = input("Qual Letra? ")
         chute = chute.strip().upper()
         
        
         if(chute in palavra_secreta):
             index = 0
             for letra in palavra_secreta:
                 if(chute.upper() == letra.upper()):
                     letras_acertadas[index] = letra
                 index += 1             
         else:
              error += 1
         
         enforcou = error == len(palavra_secreta)
         acertou = "_" not in letras_acertadas
         print(letras_acertadas)
         
     if(acertou):
          print("Parabens voce acertou !!")
     else:
          print("Que Pena voce Perdeu Tente de novo!!!")
      
     print("O nome da Fruta é : ", palavra_secreta)
     print("Fim do Jogo")
     
if(__name__=="__main__"):
    jogar()