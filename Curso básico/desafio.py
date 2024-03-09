#Exercicio desafio
#sistema de consulta de preço

precos = [1500,1000,800,2000]
produtos = ['celular', 'camera', 'fones de ouvido', 'monitor']
# o usuario dá o nome do produto
# O sistema vai dá o preco do produto
# dizer ao usuario se existe ou não

#Passos
# 1 passo: perguntar ao usuario qual o produto
produto_usuario = input("Digite aqui seu produto: ")
produto_usuario = produto_usuario.lower()

# 2 passo: verificar se o produto está na lista de produtos 
if not produto_usuario in produtos:
    print("O seu produto não conta no estoque")
else:
    if produto_usuario == produtos[0]:
        print(f"O seu produto: {produto_usuario}, valor: {precos[0]}")
    elif produto_usuario == produtos[1]:
        print(f"O seu produto: {produto_usuario}, valor: {precos[1]}")
    elif produto_usuario == produtos[2]:
        print(f"O seu produto: {produto_usuario}, valor: {precos[2]}")
    elif produto_usuario == produtos[3]:
        print(f"O seu produto: {produto_usuario}, valor: {precos[3]}")


# 3 passo: dá o output do preco e do produto, caso não tenha o produto, dizer que não tem

# if produto_usuario in produtos
        # posicao = produtos.index(produto_usuario)
        #preco = precos[posicao]
        #print(f"produto: {produto_usuario},  preço {preco}")
    #else:
        #print("Produto não encontrado")