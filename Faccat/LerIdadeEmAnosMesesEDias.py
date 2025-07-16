print("Ler idade em anos, meses e dias")

anos = int(input ("Digite quantos anos você tem: "))
anos *= 365

meses = int(input ("Digite quantos meses: "))
meses*= 30

dias = int (input("Digite quantos dias "))

totalDeDias = anos + dias + meses

if (totalDeDias == 1):
    print(f"Você já viveu: {totalDeDias} dia")
else:
    print(f"Você já viveu: {totalDeDias} dias")

