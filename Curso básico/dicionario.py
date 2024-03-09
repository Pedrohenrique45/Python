precos = [1500,1000,800,2000]
produtos = ['celular', 'camera', 'fones de ouvido', 'monitor']
# no dicionario você passa uma chave e um valor. Melhor que lista para adicionar ligações. No dicionario tem uma chave e um valor

dic_preco = {"Celular": 1500, "Camera": 1000, "Fones de ouvido": 800, "monitor": 2000}

# Pegar um item
preco_celular = dic_preco['Celular']
print(dic_preco)

dic_preco['Celular'] = 2000
print(dic_preco)

#retirar um item
dic_preco.pop("Celular")
print(dic_preco)

# tamanho do dicionario
print(len(dic_preco))

#ver se um item está no dicionario
print("televisao" in dic_preco)

# ver se um valor está no dicionario
print( 1000 in dic_preco.values()) # valores das chaves
print(dic_preco.keys()) # valores das chaves