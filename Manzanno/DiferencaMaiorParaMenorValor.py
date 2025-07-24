print("Descobrir a diferença do maior para o menor valor\n")

valores = []
diferenca = 0

for i in range(2):
    
    valor = float(input(f"Digite o {i + 1}° valor: "))
    valores.append(valor)

if valores[0] > valores[1]:
      diferenca = valores[0] - valores[1]
else:
      diferenca = valores[1] - valores[0]

print(f"A  diferença do  menor para o  maior valor  é: {diferenca}")     