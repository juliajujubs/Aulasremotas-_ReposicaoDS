class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descricao(self):
        return f"Veículo: {self.marca} {self.modelo}"


class Carro(Veiculo): 
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas

    def descricao(self):
        return f"Carro: {self.marca} {self.modelo}, {self.numero_portas} portas"

if __name__ == "__main__":
    carro1 = Carro("Toyota", "Corolla", 4)
    print(carro1.descricao())

    carro2 = Carro("Honda", "Civic", 4)
    print(carro2.descricao())

    carro3 = Carro("Fiat", "Uno", 2)
    print(carro3.descricao())
