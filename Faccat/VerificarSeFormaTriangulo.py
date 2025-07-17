print("Validar Triângulos")

lados = []

for i in range(3):
    
    while True:
        try: 
            comprimentoLado = float(input(f"Digite o comprimento do Lado {i + 1}: "))
            if comprimentoLado <= 0:
                print("O comprimento do lado deve ser um número positivo.")
            else:
                lados.append(comprimentoLado) 
                break 
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
            
condicao1 = lados[0] + lados[1] > lados[2]
condicao2 = lados[1] + lados[2] > lados[0]
condicao3 = lados[0] + lados[2] > lados[1]

if condicao1 and condicao2 and condicao3:
    print(f"valor dos lados = {lados[0]} | {lados[1]} | {lados[2]} ")
    print("É possível  montar um triângulo")
else:
    print(f"valor dos lados = {lados[0]} | {lados[1]} | {lados[2]} ")
    print("Não é possível montar um triângulo")
