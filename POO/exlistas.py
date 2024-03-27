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
lista.remove(5)
print(lista)
