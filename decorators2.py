# def gritar(funcao):
#     def aumentar(nome):
#         return funcao(nome).upper()
#     return aumentar
# 
# @gritar
# def saudacao(nome):
#     return f'Olá, eu sou o {nome}'
# @gritar
# def solicitar(principal, acompanhamento):
#     return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'
def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar

@gritar
def saudacao(nome):
    return f'Olá, eu sou o {nome}'
@gritar
def solicitar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor'

print(saudacao('Almeida'))

print(solicitar('Lazanha', 'Vinho Branco'))

@gritar
def lol():
    return 'lol'

print(lol())