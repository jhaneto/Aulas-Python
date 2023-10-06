from pessoa_fisica import Pessoa, PessoaFisica
from pessoa_juridica import PessoaJuridica
from contabanco import ContaBanco

pessoafisica =  PessoaFisica(333,'almeida neto',22)
pessoajuridica = PessoaJuridica(50050, 'joao pedro', 23)
pessoa = Pessoa('paulo', 12)
contabanco = ContaBanco(123, "almeida",25, 200.0, 100.0)

print("     Pessoa Fisica      ")
print(('*')*30)
print(pessoafisica.getNome())
print(pessoafisica.idade)
print(pessoafisica.CPF)

print("     Pessoa Juridica   ")
print(('*')*30)
print(pessoajuridica.getNome())
print(pessoajuridica.idade)
print(pessoajuridica.CNPJ)
pessoajuridica.setCNPJ(500)

print(pessoajuridica.getCNPJ())

print("     Conta Banco   ")
print(('*')*30)
print(contabanco.numero)
contabanco.setNumero(23456)
print(contabanco.getNumero())
print(contabanco.getNome())
print(contabanco.idade)
print(contabanco.saldo)
print(contabanco.limite)

print(contabanco.extrato())

print("     Conta Banco   ")
print(('*')*30)
contabanco.deposita(50.0)
print(contabanco.getNome())
print(contabanco.idade)
print(contabanco.saldo)
print(contabanco.limite)

contabanco.saca(500.0)
print(pessoa.nomeMaiu)