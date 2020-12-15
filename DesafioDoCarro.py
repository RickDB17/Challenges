"""
Desafio de fim de semana I


 Implemente uma classe chamada Carro com as seguintes propriedades:

1 - Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma
certa quantidade de combustível no tanque.
2 - O consumo é especificado no construtor e o nível de combustível inicial é 0.
3 - Forneça um método andar( ) que simule o ato de dirigir o veículo por uma 
certa distância, reduzindo o nível de combustível no tanque de gasolina.
4 Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
5- Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de 
uso:

meuFusca = Carro(15);           # 15 quilômetros por litro de combustível. 
meuFusca.adicionarGasolina(20); # abastece com 20 litros de combustível. 
meuFusca.andar(100);            # anda 100 quilômetros.
meuFusca.obterGasolina()        # Imprime o combustível que resta no tanque.
"""

name = input("Diga o modelo do seu carro:\n»»» ")
tank = input("Diga o volume atual de combustível:\n»»» ")
consume = input("Diga o consumo de litros por quilômetro de seu automóvel:\n»»» ")

class Carro:
    def __init__(self, name, tank, consume):
        self.nome = name
        self.tanque = tank
        self.consumo = consume

    def obterGasolina(self):
        print(self.tanque)

    def adicionarGasolina(self):
        gasolina = int(input("Quantos litros você deseja adicionar?\n»»» "))
        self.tanque = self.tanque + gasolina
        print(f"Foi adicionado {gasolina} ao seu tanque, que agora apresenta {self.tanque}.")

    def andar(self):
        distancia = int(input("Quantos quilômetros você deseja andar?\n»»» "))
        self.tanque = self.tanque - (distancia/self.consumo)
        print(f"Você andou {distancia}, tanque atual: {self.tanque}.")

def game():
    a = int(input("1. Ver tanque\t|2. Encher tanque\t|3. Andar"))
    if a == 1:
        car.obterGasolina()
        game()
    elif a == 2:
        car.adicionarGasolina()
        game()
    elif a == 3: 
        car.andar()
        game()
    

car = Carro(name, tank, consume)
game()
