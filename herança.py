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
class Bruxo:
    def __init__(self, casa, patrono):
        self.casa = casa
        self.patrono = patrono
    
    def lançarFeitico(self):
        return(f'lançou feitiço: expectro patronom - {self.patrono}')

class Mestico(Trouxa, Bruxo):
    def __init__(self, nome, cpf, casa, patrono):
        super().__init__(nome, cpf)
        Bruxo.__init__(self, casa, patrono)

    def lançarFeitico(self):
        return(f'{self.nome} lançou feitiço: expectro patronom - {self.patrono}')
    
mestico1 = Mestico('Luna Lovegood', '001.001.000.11', 'Grifinoria', 'Coelho')

print(mestico1.lançarFeitico())