class Veiculo:
    def __init__(self, marca, modelo, anoFab, preco):
        self.marca = marca
        self.modelo = modelo
        self.anoFab = anoFab
        self.preco = preco

    def ExibirInformacoes(self):
        return (f'Marca: {f"{self.marca}":<10} '
                f'Modelo: {f"{self.modelo}":<20}'
                f'Ano de fabricação: {f"{self.anoFab}":<10} '
                f'Preço: {f"{self.preco}":<10}')


class Carro(Veiculo):
    def __init__(self, marca, modelo, anoFab, preco, numPortas, combustivel):
        super().__init__(marca, modelo, anoFab, preco)
        self.numPortas = numPortas
        self.combustivel = combustivel
    
    def ExibirInformacoes(self):
        return (f'Marca: {f"{self.marca}":<10} '
                f'Modelo: {f"{self.modelo}":<20}'
                f'Ano de fabricação: {f"{self.anoFab}":<10} '
                f'Preço: {f"{self.preco}":<10}'
                f'Numero de Portas: {self.numPortas}    '
                f'Combustivel: {self.combustivel}')
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, anoFab, preco, cilindrada, partida):
        super().__init__(marca, modelo, anoFab, preco)
        self.cilindrada = cilindrada
        self.partida = partida
    
    def ExibirInformacoes(self):
        return (f'Marca: {f"{self.marca}":<10} '
                f'Modelo: {f"{self.modelo}":<20}'
                f'Ano de fabricação: {f"{self.anoFab}":<10} '
                f'Preço: {f"{self.preco}":<10}'
                f'Cilindrada: {self.cilindrada}    '
                f'Partida: {self.partida}')

class Concessionaria():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.__listaVeiculos = []
    
    def AddVeiculo(self, novoVeiculo):
        self.__listaVeiculos.append(novoVeiculo)
        print('veiculo adiocionado')

    def ListarTodos(self):
        for indice in self.__listaVeiculos:
            print(indice.ExibirInformacoes())


moto1 = Moto('yamaha', 'factor 125ks', 2012, 6500, 124, 'eletrica e pedal')
moto2 = Moto('honda', 'cb twister', 2012, 22500, 250, 'eletrica')
moto3 = Moto('yamaha', 'fazer 150s', 2012, 12500, 150, 'eletrica')
moto4 = Moto('kawasaki', 'Z400', 2024, 34500, 400, 'eletrica')
moto5 = Moto('bmw', 'GS 300', 2023, 65500, 300, 'eletrica')
carro1 = Carro('bmw', 'i7', 2024, 1000000, 5, 'eletrico')
carro2 = Carro('audi', 'A4', 2024, 100000, 5, 'gasolina')
carro3 = Carro('honda', 'civic', 2024, 1000000, 5, 'flex')
carro4 = Carro('dodge', 'charger', 2024, 1000000, 5, 'gasolina')
carro5 = Carro('fiat', 'pulse abath', 2024, 1000000, 5, 'gasolina')
concessionaria1 = Concessionaria('Dieguinho Veiculos', 'rua arauto, n° 123')

concessionaria1.AddVeiculo(moto1)
concessionaria1.AddVeiculo(moto2)
concessionaria1.AddVeiculo(moto3)
concessionaria1.AddVeiculo(moto4)
concessionaria1.AddVeiculo(moto5)
concessionaria1.AddVeiculo(carro1)
concessionaria1.AddVeiculo(carro2)
concessionaria1.AddVeiculo(carro3)
concessionaria1.AddVeiculo(carro4)
concessionaria1.AddVeiculo(carro5)
print(concessionaria1.ListarTodos())