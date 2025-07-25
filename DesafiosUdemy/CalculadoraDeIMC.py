print("Calculadora de IMC")

peso = float(input("Digit seu peso: "))

altura = float(input("Digite sua altura: "))

valorImc = peso / (altura ** 2)

if valorImc < 18.5:
    print("Magreza")
    print(f'Valor do IMC: {valorImc:.2f}')
    
elif valorImc > 18.5 and valorImc < 24.9:
    print("Peso Normal")
    print(f'Valor do IMC: {valorImc:.2f}')
    
elif valorImc > 25 and valorImc < 29.9:
    print("SobrePeso")
    print(f'Valor do IMC: {valorImc:.2f}')
    
elif valorImc > 30 and valorImc < 39.9:
    print("Obesiidade")
    print(f'Valor do IMC: {valorImc:.2f}')
    
else:
    print("Obesidade Grave")
    print(f'Valor do IMC: {valorImc:.2f}')