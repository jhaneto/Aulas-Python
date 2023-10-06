from pessoa import Pessoa

class ContaBanco(Pessoa):
    def __init__(self, numero, nome, idade, saldo, limite):
        super().__init__(nome, idade)
        print("Construindo Objeto...{}".format(self))
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
        
    def getNumero(self):
        return  self.numero
    
    def setNumero(self, numero):
        self.numero = numero
        
    def extrato(self):
        print("Saldo do {} do Nome do Titular {}".format(self.saldo, self.nome))
        
    def deposita(self, valor):
        self.saldo += valor
        
    def saca(self, valor):
        if (valor >= (self.saldo + self.limite)):
            print(f"Você Não tem Saldo pra Sacar esse Valor,  Valor Atual: {self.saldo} ")
        else:    
            self.saldo -= valor