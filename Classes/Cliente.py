class Cliente:
    # construtor
    def __init__(self, nome, email, cpf, endereco):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.endereco = endereco
    
    # método de instância que retorna uma string com as informações do cliente
    def info(self):
        return f'Nome:\t {self.nome}\nEmail:\t {self.email}\nCPF:\t {self.cpf}'
    

