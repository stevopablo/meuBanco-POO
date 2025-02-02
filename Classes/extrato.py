import datetime as dt


class Extrato:
    def __init__(self):
        self.__transacoes = []
    
    def adicionar_transacao(self, tipo, valor):
        self.__transacoes.append((tipo, valor, dt.datetime.today()))
    
    def gerar_extrato(self, conta):
        print(f'Extrato da conta {conta.numero} de {conta.titular}')
        print('--------------------------------')
        for trans in self.__transacoes:
            print(f'{trans[0]:15} {trans[1]} {trans[2].strftime("%d/%m/%Y %H:%M:%S")}')
