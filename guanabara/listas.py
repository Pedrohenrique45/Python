valor = []

for cont in range(0,5):
    valor.append(int(input('Digite um número: ')))

print(valor)

dados = []
dados.append('pedro')
dados.append('19')
pessoas = list()
pessoas.append(dados[:]) #adiciona uma lista dentro de outra lista, ele cria uma copia dentro de outra lista então elas está interligadas

pessoas = [['pedro', 25], ["Maria", 19], ["joão", 20]]
print(pessoas[0][0])
print(pessoas[1][1])

for p in pessoas:
    print(f"{p[0]} tem {p[1]} anos de idade")