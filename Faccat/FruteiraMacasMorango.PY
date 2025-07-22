print("Calcular preço da compra de frutas do cliente\n\n")

macasCompradas = float(input("Quantidade de morangos comprados (kg): "))

morangosComprados = float(input("Quantidade de maçãs compradas (kg): "))

pesoTotal = macasCompradas + morangosComprados

if (macasCompradas  <= 5 and macasCompradas > 0 ):
    print(f"Valor da maçã por kg R$1,80")
    precoMacas = macasCompradas * 1.8

else :
    print(f"Valor da maçã por kg R$1,50")
    precoMacas = macasCompradas * 1.5
    
if (morangosComprados  <= 5 and morangosComprados > 0 ):
    print(f"Valor do morango por kg R$2,5")
    precoMorangos = morangosComprados * 2.5
    
else :
    print(f"valor do morango por kg R$2,20")
    precoMorangos = morangosComprados * 2.2
    
valorTotal = precoMacas + precoMorangos

if (pesoTotal > 8 or valorTotal >  25):
    valorTotal =valorTotal * 0.1 + (valorTotal)
    print(f"Valor a pagar:  R${valorTotal}")
else:
    print(f"Valor a pagar:  R${valorTotal}")
    
    