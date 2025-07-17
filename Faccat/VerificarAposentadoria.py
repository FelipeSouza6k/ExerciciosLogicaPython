import datetime

print("Verificar se funcionário esta apto para aposentadoria")

nomeFuncionario = input("Digite o nome do Funcionário: ")

tempoDeEmpresaFuncionario = int(
    input("Digite a quantos anos o funcionário esta na empresa: ")
)

idadeFuncionario = int(input("Digite a quantos anos o funcionário esta na empresa: "))

tempoEmpresa = datetime.datetime.now().year
tempoEmpresa -= tempoDeEmpresaFuncionario

if (tempoEmpresa > 30 or idadeFuncionario > 65) and (
    idadeFuncionario > 60 and tempoDeEmpresaFuncionario > 25
):
    print(f"Funcionário:{nomeFuncionario}\n Aposentadoria: Apto a aposentar")
else:
    print("Não requer aposentadoria")
