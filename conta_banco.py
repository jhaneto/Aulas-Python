from operator import attrgetter


class Conta:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
        
    def depositar(self, valor):
        self._saldo += valor
        
#     def __eq__(self, outro):
#         return self._codigo == outro._codigo and self._saldo == outro._saldo
    def __lt__(self, outro):
        return self._saldo < outro._saldo
    
    def __eq__(self, outro):
        if self._codigo == outro._codigo and self._saldo == outro._saldo:
            return "A conta tem o mesmo codigo"
        return "Parabens pela abertura de conta"
    
    def __str__(self):
        return "[<< Codigo {} Saldo {} >>".format(self._codigo, self._saldo)
     
    
conta1 = Conta(37)
conta2 = Conta(38)
conta1.depositar(500)
conta2.depositar(1000)
# if conta1 == conta2:
#     print("Contas Iguais")
print(conta1 > conta2)
print(conta1._saldo)
print(conta2)