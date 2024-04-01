#Escreva um programa que encontre todos os números divisíveis por 7, mas que não sejam múltiplos de 5, entre 2.000 e 3.200 (ambos incluídos). Os números obtidos devem ser impressos em sequência separada por vírgula em uma única linha.

#Um número é divisível por 7 quando:  se o dobro do seu último algarismo subtraído do número sem o último algarismo, resulta em um número divisível por 7
l = []

for i in range(2000,3200):
   if (i%7 == 0) and  (i%5 != 0):
      l.append(i)

print(l)