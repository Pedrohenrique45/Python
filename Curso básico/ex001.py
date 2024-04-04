print("---Progressão áritimetrica----")
numero_inicial = float(input("Qual o primeiro termo: "))
razão = float(input("Qual a razão:" ))

contador = numero_inicial
print(contador)
for i in range(10):
    contador = contador + razão
    i = i + 1
    print(contador)
