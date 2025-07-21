cores = ["amarelo", "verde", "azul", "roxo"]

corCliente = input("Digite uma cor: ")

if corCliente.lower() in cores:
    print("Cor esta em estoque ")
else:
    print("Está cor esta esgotada")