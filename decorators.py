def seja_educado(funcao):
    def sendo_ok():
        print('Foi Legal conhecer vc ')
        funcao()
        print('tenha um Bom dia')
    return sendo_ok


@seja_educado
def apresentado():
     print('Ola Marcos')
    

apresentado()