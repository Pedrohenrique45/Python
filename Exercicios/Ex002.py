#Escreva um programa que possa calcular o fatorial de um determinado número. Os resultados devem ser impressos em sequência separada por vírgula em uma única linha. Suponha que a seguinte entrada seja fornecida ao programa: 8 Então, a saída deveria ser: 40320
def fatorial(x):
    if x == 0:
        return 1
    return x * fatorial(x -1)

valor = int(input("Qual o fatorial? "))
print(fatorial(valor))