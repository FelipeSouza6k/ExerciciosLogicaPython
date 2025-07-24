import statistics
#Biblioteca utilizada para calcular a média
print("Calcular Média")

notas = []

for i in range(4):
    valor = float(input(f"Digite a {i + 1}° nota: "))
    notas.append(valor)

media = statistics.mean(notas)

print(f"Média: {media:.2f}")

if media < 7:
    print("Necessário exame\n")
    mediaExame = float(input("Digite a nota do exame "))
    
    notas.append(mediaExame)
    
    media = statistics.mean(notas)
    
    print(f"Média = {media:.2f}\nAprovado em exame") if media > 5 else print(f"Média = {media:.2f}\nReprovado")
    
else: 
    print("Aluno aprovado (Não há necessidade de exame)")