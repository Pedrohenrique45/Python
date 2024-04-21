vendedores = ["Pedro", "Marcos", "João", "Mário"]
vendas = [34, 21, 14, 15]

for venda, vendedor in enumerate(vendedores):
    print(vendedor) #percorre a parte da lista de vendedor
    print(vendas[venda]) #percorrer a lista de vendas, pega o número correspondente na lista


valores = []
valores.append(5)
valores.append(4)
valores.append(9)

for c, v in enumerate(valores):
    print(f"na posição {c} encontrei o valor {v}")
    #o valor c percorrer as posições e o valor v a lista

print('chegeui ao final da lista ')
