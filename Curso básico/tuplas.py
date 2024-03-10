def calcular_imposto2(preco, ir=0.75, csll=0.035,iss=0.05):
    imposto_ir = preco * ir
    imposto_csll = preco * csll 
    imposto_iss = preco * iss
    return imposto_ir, imposto_csll,imposto_iss

resposta = calcular_imposto2(1000)
ir,csll,iss = resposta # pega os três valores de uma vez só
print(ir, csll, iss, sep="\n")

tamnho_tela = (1920,1080)
#valores fixo



# uma tupla é quando uma função retorna mais de um valor como resposta - lista de informações 
# a diferença é que uma tupla é  imútavel 

#processo de unpaking da tupla