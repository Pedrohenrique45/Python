faturamento = 1000
custo = 2000

lucro = faturamento - custo

#if comparação (condição)
if lucro >= 0:
    #tudo que acontece se condição for verdadeira
    print("lucro:", lucro)
else:
    #tudo que acontece se if for falso
    print("prejuizo de:", lucro)


produtos  = ["iphone", "ipad", "airdorp"]
novo_produto = input("Digite aqui o produto: ")
novo_produto = novo_produto.lower()

if novo_produto in produtos:
    #in identifica se o produto está dentro da variavel produtos
    print("Produto já registrado")
else:
    print("Produto nã cadastrado")
    produtos.append(novo_produto)

print(produtos)