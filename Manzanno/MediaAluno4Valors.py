import statistics
#Biblioteca utilizada para calcular a média

print("Calcular Média")

notas = []

for i in range(4):
    valor = float(input(f"Digite a {i + 1}° nota: "))
    notas.append(valor)

media = statistics.mean(notas)

print(f"Média: {media}")

print("Aluno aprovado") if media > 4.99 else print("Aluno reprovado")