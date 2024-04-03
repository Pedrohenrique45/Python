#Pergunta: Escreva um programa que aceite uma sequência de números separados por vírgula do console e gere uma lista e uma tupla que contenha cada número. Suponha que a seguinte entrada seja fornecida ao programa: 34,67,55,33,12,98 Então, a saída deve ser: ['34', '67', '55', '33', '12', ' 98'] ('34', '67', '55', '33', '12', '98')

valor = input('digite uma lista de números: ')
lista = valor.split(",")
tupla = tuple(lista)
print(lista)
print(tupla)