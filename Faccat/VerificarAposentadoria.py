import datetime

print("Verificar se funcionário esta apto para aposentadoria")

nomeFuncionario = input("Digite o nome do Funcionário: ")
 
ingressoFuncionario = int(
    input("Digite o ano de ingresso do funcionário na empresa: ")
)

anoNascimentoFuncionario = int(input("Digite o ano de nascimento do funcionário: "))
 
tempoEmpresa = 2025 - ingressoFuncionario
idadeFuncionario = 2025 - anoNascimentoFuncionario

if (tempoEmpresa > 30 or idadeFuncionario > 65) :
    print(f"Funcionário: {nomeFuncionario}\nAposentadoria: Apto a aposentar")
elif (idadeFuncionario > 60 and tempoEmpresa > 25):
    print(f"Funcionario: {nomeFuncionario}\nRequer aposentadoria")
else:
    print(f"Funcionario: {nomeFuncionario}\nNão requer aposentadoria")
