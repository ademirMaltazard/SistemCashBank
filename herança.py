class Trouxa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.__cpf = cpf

    def cumprimentar(self):
        print(f"olá! Tudo bem? me chamo {self.nome}")

    def setCpf(self, novoCpf):
        self.__cpf = novoCpf
    
    def getCpf(self):
        return self.__cpf

# Criação classe Mae que herda atributos da classe Pessoa
