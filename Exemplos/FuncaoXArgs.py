def numerosSoma (*numeros):
    resultado = 0
    #quando se coloca o * antes de um argumento ele permite adicionar varios números, não apenas 1.
    for valor in numeros:
        resultado += valor
        
    print(resultado)

numerosSoma(3,5)
