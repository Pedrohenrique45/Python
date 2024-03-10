lista_precos = [1500, 1000, 8000, 2000]


total_imposto = 0

def calcular_imposto(preco, aliquota1=0.2, aliquota2=0.15,aliquota3=0.1):
    if preco > 1000:
        imposto = preco * aliquota1
    elif preco > 1000:
        imposto = preco * aliquota2
    else:
        imposto = preco * aliquota3
    return imposto  #para levar a variavel para fora da função


for preco in lista_precos:
    imposto  = calcular_imposto(preco,aliquota1=0.14) 
    total_imposto = total_imposto + imposto
   
print(total_imposto)

#def funcao()

def se_increve():
    print("se inscreve")

for i in range(10):
    se_increve()


def calcular_imposto2(preco, ir=0.75, csll=0.035,iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll 
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll,imposto_iss

resposta = calcular_imposto2(1000)

print(resposta)
