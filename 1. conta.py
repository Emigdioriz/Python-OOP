# Estudo inicial de POO 

class Conta: 
    def __init__ (self, numero, titular, saldo, limite): 
        print("Construindo objeto ... {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    # introdução dos métodos
    def extrato(self):
        print("Saldo do titular {} é : {}".format(self.titular, self.saldo))

    def depositar(self, valor):
        self.saldo += valor
        print("Valor de {} depositado com sucesso".format(valor))

    def sacar(self, valor):
        self.saldo -= valor
        print("Valor de {} sacado com sucesso".format(valor))


conta = Conta(123, 'emigdio', 1000, 1000)

# para obter acesso a uma informação do objeto basta: 
print(conta.saldo)




