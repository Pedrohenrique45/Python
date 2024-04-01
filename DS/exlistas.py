# comprimento da lista
lista = [1,2,3,4,5]
print(lista)
# as listas da visão de python são vistas como objetos com o tipo de dados de list
# <class 'list>
print(type(lista))
#é possivel usar o contrutor lista, para conseguir criar novas listas: list()
#são coleções mutáveis e ordenaveis, no  python, e permite membros duplicados 
#indexação negativa, significa pegar o último número da lista
print(lista[-1])
#intervalo de índices
print(lista[2:4])

#verificar a existência do item
if 3 in lista:
    print('O item está na lista')

#alterar valor da lista
    
lista[2] = 4
print(lista)

#inserir um novo item

lista.insert(3, "pedro")
print(lista)

#adiciona  e remover item na lista
lista.append(6)

lista.remove(5) #remover item especificado
lista.pop(1)#remover item pelo indice / pilha
del lista[2]#também remove item especificado e sem o colchetes podem apagar toda a lista
# lista.clear() limpa a lista
print(lista)


lista_1 = [9,9,2,2,4,5]
for i in lista_1:
    print(i)

for i in range(len(lista_1)):
    print(lista[i])


# compreensão de lista

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# novalista = [expressão for item in interable if condição==True]

#Classificar Alfanumericamente
lista.sort()

#Classificar em ordem decrescente
lista.sort(reverse=True)

#Classificar em ordem revesar
lista.reverse()