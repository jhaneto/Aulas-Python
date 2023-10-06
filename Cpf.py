class CPF:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_valida(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF invalido")
        
        self.fatiamento(self.cpf)
        
    def cpf_valida(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False
    def validar_numero(self, num):
        cpf_num = "[0-9]{4,5}[-]*[0-9]{4}"
    def fatiamento(self):
        fatia_cpf1 = cpf[:3]
        fatia_cpf2  = cpf[3:6]
        fatia_cpf3 = cpf[6:9]
        fatia_cpf4 = cpf[9:]
        cpf_formatado = "{}.{}.{}-{}".format(fatia_cpf1,fatia_cpf2,fatia_cpf3,fatia_cpf4)
        return  cpf_formatado