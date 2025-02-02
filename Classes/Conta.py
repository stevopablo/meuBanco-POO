import datetime as dt
from Classes.extrato import Extrato


class Conta:
    # construtor
    def __init__(self, clientes, numero, titular, saldo):
        self.clientes = clientes
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__data_abertura = dt.datetime.today()
        self.__extrato = Extrato()

    
    def mostrar_saldo(self):
        return self.__saldo
    
    def extrato(self):
        self.__extrato.gerar_extrato(self)
    
    def deposita(self, valor):
        self.__saldo += valor
        print(f"Depósito de {valor} realizado com sucesso")
        self.__extrato.adicionar_transacao('Depósito', valor)

    def saca(self, valor):
        if self.__saldo < valor:
            print(f"Saldo insuficiente")
            return False
        else:
            self.__saldo -= valor
            print(f"Saque de {valor} realizado com sucesso")
            self.__extrato.adicionar_transacao('Saque', valor)
            return True

    def transfere(self, valor, destino):
        if self.saca(valor):
            destino.deposita(valor)
            print(f"Transferência de {valor} realizada com sucesso para {destino.titular}")
            self.__extrato.adicionar_transacao('Transferência', valor)
            return True
        else:
            print(f"Saldo insuficiente")
            return False

     # Métodos getter e setter para os atributos privados

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def numero(self):
        return self.__numero

    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
