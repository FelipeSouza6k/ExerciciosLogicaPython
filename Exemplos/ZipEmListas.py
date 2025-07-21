# Juntar os mesmos index de listas diferentes

cores = ["verde", "amarelo", "azul", "vermelho"]
valores = [10, 20, 30, 40]

listasJuntas = zip(cores, valores)

print(list(listasJuntas))
#Saída = [('verde', 10), ('amarelo', 20), ('azul', 30), ('vermelho', 40)]
