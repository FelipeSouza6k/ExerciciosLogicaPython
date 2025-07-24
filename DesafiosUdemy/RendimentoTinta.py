def rendimento (largura, altura, rendimento):
    quantidadeLatas = largura * altura / rendimento 
    if quantidadeLatas == 1:
        print(f"Será necessário 1 lata de tinta ")
    else:
        print(f"Serão necessáras {quantidadeLatas} latas de tinta ")
        
#Fim função rendimento

print ("Calcular quantas latas de tinta são necessárias para pintar uma parede")

while True:
    entradaLargura  = input("Digite a largura da parede: ")
    try:  
        largura = int(entradaLargura)
        break 
    except ValueError:
        print("Valor Inválido, digite novamente")

while True:
    entradaAltura = input("Digite a altura da parede: ")
    try: 
        altura = int(entradaAltura)
        break 
    except ValueError:
         print("Valor Inválido, digite novamente")

while True:
    entradaRendimento  = input("Digite o rendimento da lata de tinta:")
    try: 
        rendimentoLata = int(entradaRendimento)
        break 
    except ValueError:
            print("Valor Inválido, digite novamente")
        
rendimento(largura, altura, rendimentoLata)