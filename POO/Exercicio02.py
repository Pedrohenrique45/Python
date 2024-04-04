def calcularCelsius(temperatura):
    valor = ((temperatura - 32) * 5)/9 #passar o valor em far
    return valor

def calcularFar(temperatura):
    valor = ((temperatura * 9)/5) + 32 #passar o valor em celsius
    return valor

temperatura = float(input("Digite a temperatura: "))
print(f"Valor de fahrenheit para celsius: {calcularCelsius(temperatura)}")
print(f"Valor de celsius para fahrenheit: {calcularFar(temperatura)}")




    

