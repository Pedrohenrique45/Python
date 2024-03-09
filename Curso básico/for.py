#for item in lista:
    #o que quer escrever

for i in range(10):
    print("Pedro")

lista_precos = [1500, 1000, 8000, 2000]
imposto = 0.1

for preco in lista_precos:
    preco *= imposto
    print(preco)

# regra do imposto
    
for preco in lista_precos:
    if preco > 1000:
        imposto = 0.15
    else:
        imposto = 0.1
    preco *= imposto
    print(preco)

#total do imposto
    
total_imposto = 0
for preco in lista_precos:
    if preco > 1000:
        imposto = preco * 0.15
    else:
        imposto = preco * 0.1
    print(preco)
    total_imposto = total_imposto + imposto
   
print(total_imposto)