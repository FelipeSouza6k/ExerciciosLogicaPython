import statistics 
print("---Verificar média de preço das mercadorias em estoque---")

mercadoriasEstoque = int(input("Quantidade de mercadorias em estoque: "))
valorMercadorias = []

print("Digite os valores das mercadorias")

for valor in range(mercadoriasEstoque):
    while True: #Loop criado para impedir que o usuário digite valoes inválidos
        entradaValor = input("Valor: ")
        try:
            valor = float(entradaValor)
            valorMercadorias.append(valor)
            break
        except ValueError: #ValueError é o tipo do erro que ocorre quando o usuario digita uma string ao invés de um float
            print("Valor inválido, digite novamente.")   
            
mediaValores = statistics.mean(valorMercadorias)

print(f"\n---Média dos valores das mercadorias---\nMédia: {mediaValores}")
    
    
    
