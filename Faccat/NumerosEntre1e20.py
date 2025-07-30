print("---Verificar números entre 10 e 20---")

valores = []

for i in range(10):
    
    valor = float(input("Digite um valor: "))
    if valor > 10 and valor < 20:
        valores.append(valor)
        
print("Valores digitados q estão entre 10  e 20:")

for j in valores:
    print(j)

    

