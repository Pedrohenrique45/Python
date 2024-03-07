vendas = [100, 50,120 , 130, 80, 10]

print(vendas[-1]) # conta da direita para esquerda, ou seja dá para pegar o ultimo elemento

total_vendas = sum(vendas)
print(total_vendas)
quantidade = len(vendas)
print(quantidade)
valor_max = max(vendas)
valor_min = min(vendas)
print(valor_max, valor_min)

posicao = vendas.index(130)
print(posicao)

produto = ["iphone", "ipad",]

print("iphone" in produto) # o in é lido como contém

produto_usuario = input("Digite um nome de um produto? ")
print(produto_usuario in produto)

##operações em listas

# edita um item
preco  = [100, 400, 2000]
preco[0] = 4000
print(preco)
preco = preco[0] *1.1
print(preco)

#adiciono um item
produto.append("mackbook")

#retirar um item
produto.remove("mackbook")
preco.pop(-1)
print(preco)

#inserir um valor
produto.insert(1, "airpod")
print(produto)

# contar valores
print(produto.count("airpod"))

# ordenar
preco.sort(reverse = True)
print(preco)