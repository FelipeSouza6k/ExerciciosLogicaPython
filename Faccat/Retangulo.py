print("Calcular área de um retángulo")

while True:
    entradaAltura = input("Digite a altura: ")
    try:
        altura = int(entradaAltura)
        break
    except ValueError:
        print ("Valor da da altura inválida")
        
while True:
    entradaBase = input("Digite a base: ")
    try:
        base = int(entradaBase)
        break
    except ValueError:
        print("Valor da base inválida")
         
print(f"Área do retangulo é: {base * altura}")

