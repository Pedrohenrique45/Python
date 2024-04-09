#Escreva um programa que calcule e imprima o valor de acordo com a fórmula fornecida: Q = Raiz quadrada de [(2 * C * D)/H] A seguir estão os valores fixos de C e H: C é 50. H é 30 D é a variável cujos valores devem ser inseridos em seu programa em uma sequência separada por vírgulas. Exemplo Vamos supor que a seguinte sequência de entrada separada por vírgula seja fornecida ao programa: 100.150.180 A saída do programa deve ser: 18,22,24

import math
c=50
h=30
value = []
items=[x for x in input("Digite um valor: ").split(',')] #Lambda 
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print(','.join(value))