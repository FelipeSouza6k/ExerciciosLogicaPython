print("DIGITE UM NÚMERO PARA DESCOBRIR SEU ANTECESSOR")
while True:
    entrada = input("Digite o valor: ")
    try:
        numero = int(entrada)
        break
    except ValueError:
        print("Entrada Inválida, digite novamente")
print( f"Antecessor de {numero} é : {numero - 1}")

