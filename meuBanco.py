# Description: Arquivo principal do projeto
from Classes.Cliente import Cliente
from Classes.Conta import Conta


# criandos clientes (instanciando objetos da classe Cliente)
c1 = Cliente('João', 'joao@email.com', '12345678901', 'Rua ABC, 123')
print(c1.info())
print('')

c2 = Cliente('Maria', 'maria@email.com', '12345678901', 'Rua ABC, 123')
print(c2.info())
print('')

c3 = Cliente('José', 'jose@email.com', '12345678901', 'Rua ABC, 123')
print(c3.info())
print('')

c4 = Cliente('Ana', 'ana@email.com', '12345678901', 'Rua ABC, 123')
print(c4.info())
print('')

conta1 = Conta([c1,c2], 1, c1.nome, 1000)
conta2 = Conta([c3,c4], 2, c4.nome, 1000)

conta1.extrato()
conta2.extrato()

print('')

conta1.deposita(100)

conta1.extrato()
conta1.saca(500)
conta1.extrato()

conta2.deposita(5000)
conta2.extrato()
conta1.transfere(500, conta2)

conta1.extrato()