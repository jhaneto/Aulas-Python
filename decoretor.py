def decoretor(funcao):
    def wrapper():
        print('Antes')
        funcao()
        print('Depois')
    return wrapper

@decoretor
def parabenizar():
    print('Parabens almeida')
    
    
# resultado = decoretor(parabenizar)
# 
# resultado()

parabenizar()