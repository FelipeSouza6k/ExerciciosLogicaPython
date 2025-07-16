
print("Digite o valor dos três lados")

lados = []

for i in range(3):
    valor = int(input(f"Diite o valor do {i + 1}° valor: "))
    lados.append(valor)

condicao1 = lados[0] + lados[1] > lados[2]
condicao2 = lados[1] + lados[2] > lados[0]
condicao3 = lados[0] + lados[2] > lados[1]

if (condicao1 and condicao2 and condicao3):
    print(f"valor dos lados = {lados[0]} | {lados[1]} | {lados[2]} ")
    print("É possível  montar um triângulo")
else:
    print(f"valor dos lados = {lados[0]} | {lados[1]} | {lados[2]} ")
    print ("Não é possível montar um triângulo")

   


