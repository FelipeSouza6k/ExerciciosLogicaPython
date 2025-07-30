import statistics 

print("---Média Aritmética dos numeros entre 15 e 100---")

numeros = list(range(15,101))

media = statistics.mean(numeros)

print(f"Média: {media}") 
    