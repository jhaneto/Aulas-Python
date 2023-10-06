def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
               return f'Valor incorretor! Primeiro argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna

@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    print(args)
    
@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2


print(soma_dez(10,12))
print(soma_dez(1, 12))

print(comida_favorita('pizza', 'churrasco'))
print(comida_favorita('saduiche', 'pizza'))     
    
            
                
                