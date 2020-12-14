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
"""
carro = ""
emoji = ""
consumo = ""

def iniciar():
    print("Bem-vindo ao simulador de consumo de combustível!")
    print("Vrum, vrum! 🚘")
    carro = input("Diga qual o modelo de seu carro!\n»»» ")
    emoji = int(input("Escolha um emoji para ele, escolha com um número:\n\
1.🚘\t2.🚗\t3.🚕\n\
4.🚙\t5.🏎️\t  6.🚓\n\
7.🚚\t8.🚛\t9.🚔\n\
10.🚖\t11.🚍\n\
»»»» "))
    consumo = int(input("Quantos Quilômetros por litro o seu carro consome? (Apenas número)\n»»» "))

iniciar()
"""
def game():
    op = int(input("Escolhas uma das opções abaixo:\n1.Encher tanque\n2.Verificar Tanque\n3. Andar x Km."))

    if op == 1:
        i = int(input("Quantos litros você deseja encher?"))
        Carro.adicionarGasolina(i)
    elif op == 2:
        Carro.obterGasolina()
    elif op == 3:
        q = int(input("Quandos quilômetros você deseja andar?"))
        Carro.andar(q)
    else:
        print("Digite: 1, 2 ou 3! >:(")
        game()

class Carro():

    def variáveis():
        name = input("Qual o nome do seu carro?\n»»» ")
        consumo = int(input("Quantos quilômetros por litro o seu carro faz\n»»» "))
        gasolina = int(input("Qual o tamanho do tanque? (Em litros)\n»»» "))

    def obterGasolina():
        print(gasolina)

    def adicionarGasolina(litros):
        gasolina = gasolina + litros

    def andar(distância):
        gasolina = gasolina - (distância/consumo)

print("Esse é o seu carro, 🚗")

Carro.variáveis()
game()


        

"""
Abstração:

Consumo = Quilômetros/litro
litragem == Quilômetros/Consumo
"""
