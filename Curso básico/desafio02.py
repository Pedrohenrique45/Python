# mesmo desafio só que usando dicionario
dic_preco = {"celular": 1500, "camera": 1000, "fones de ouvido": 800, "monitor": 2000}

produtos_usuario = input("Digite um produto:")
produtos_usuario = produtos_usuario.lower()


if produtos_usuario in dic_preco:
    preco = dic_preco[produtos_usuario]
    print(f"O produto: {produtos_usuario}, valor: {preco}")
else:
    print('Este produto não consta no estoque, por favor tente novamente')