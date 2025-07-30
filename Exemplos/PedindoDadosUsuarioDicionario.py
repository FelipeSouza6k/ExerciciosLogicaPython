print("----Ficha de cadastro----")

fichaCadastro = ['nome','sobrenome','idade','curso']

informacoesUsuario= {}

for dado in fichaCadastro:
    
    valor = input(f"Digite ({dado}):")
    
    informacoesUsuario[dado] = valor

print("Cadastro concluído\n")

print("Dados fornecidos:")

for chave, valor in informacoesUsuario.items(): #.items() permite vc trazer a key e o value
    
    print(f"{chave}: {valor}")