#SETS NÃO POSSUEM INDEX
lista1 = set([10, 20, 30, 40, 50])

lista2 = set([10, 20, 30, 70])

print(lista1 | lista2) # União entre sets

print(lista1 - lista2) # diferença entre sets

print(lista1 ^ lista2) # Apresenta os   números iguais nas sets

print(lista1 & lista2) #Aprese nta numeros similares entre as sets

print(len(lista1)) # Verificar tamanho das sets (quantos valores possui)