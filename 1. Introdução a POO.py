#%% Estudo inicial de POO 

class Conta: 
    def __init__ (self, numero, titular, saldo, limite): 
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero # colocar __ na frente do atributo é encapsular seu valor, para que so possamos ter acesso/modificar ao mesmo através dos métodos
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite # limite de saque ou tranferência

    # introdução dos métodos
    def extrato(self):
        print("Saldo do titular {} é : {}".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor
        print("Valor de {} depositado com sucesso".format(valor))

    def __pode_sacar(self, valor_a_sacar): # __ na frente do método torna-o privado, sujerindo que ele so pode ser usado por outro método
        valor_disponivel_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_saque    

    def saca(self, valor):
        if(self.__pode_sacar(valor)):    
            self.__saldo -= valor
            print("Valor de {} sacado com sucesso".format(valor))
        else:
            print("O valor {} excedeu o limite".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor) # usa o próprio objeto que chama esse método como origem da transferencia 
        destino.deposita(valor)   

    @property
    def saldo(self):
        return self.__saldo   

    @property
    def titular(self):
        return self.__titular    

    @property #atribui uma permissão a uma propiedade da classe de ser acessada diretamente com conta2.limite
    def limite(self): # substitui um get_limite
        return self.__limite

    @limite.setter #atribui uma permissão a uma propiedade da classe de ser acessada diretamente com conta2.limite = 3000
    def limite(self, limite):
        self.__limite = limite

    @staticmethod # método que é da classe, não necessita de um objeto para ser retornado. Como se fosse uma característica intrínsseca da classe. 
    def codigo_banco(): # repare que não necessita usar o self
        return "O código deste banco é 001" # método estático somente retorna o código nacional do banco 

conta = Conta(123, 'emigdio', 1000, 1000)
conta2 = Conta(124, 'mayara', 900, 1000)
Conta.codigo_banco() # aplicação do método estático 







