nomes = []

print("Bem-vindo ao adicionador de nomes!")

while True:
    nomeNovo = input("Digite um nome para adicionar à lista (ou 'sair' para encerrar): ")
    if nomeNovo.lower() == 'sair':
        nomes.sort()#Faz a lista ficar em ordem alfabética
        print("Encerrando programa. Nomes adicionados em ordem alfabética:", nomes)
        break
    else:
        nomes.append(nomeNovo)
        nomes.sort()
        print(f"'{nomeNovo}' adicionado. Lista atual em ordem alfabética : {nomes}")        