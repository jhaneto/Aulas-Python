def Triangulo(a, b, c):
    if (a > 0 and b > 0 and c > 0):
        if(a + b > c and a + c > b and b + c >  a):
             if(a == b and b == c):
                 print(f'O triangulo e equilátero a = {a} igual  b = {b} e igual c = {c}')
             elif(a == b or b == c or a == c):
                print(f'O triangulo e Isósceles a = {a} igual a b = {b} ou igual a c = {c} ou b {b} igual a {c}')
             else:
                print(f'O triangulo e Escaleno a = {a} diferente b = {b} e diferente de c = {c}')
        else:
          print('Não é um Triangulo')
    else:
        print('Não é um Triangulo')    
class name__main():
    triangulo_equilátero = Triangulo(12, 12, 12)
    triangulo_Isósceles = Triangulo(12, 12, 6)
    triangulo_Escaleno = Triangulo(12, 13, 6)
    triangulo_Noa = Triangulo(0, 12, 1)