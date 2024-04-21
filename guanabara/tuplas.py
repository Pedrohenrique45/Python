lanche = ('hamburguer', 'suco', 'pizza', 'pastel', 'pudim')

for comida in lanche:
    print(f'eu vou comer{comida}')

for cont in range(0, len(lanche)):
    print(lanche[cont])

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}")


a = (1,2,4)
b = (3,5,6,7)
c = a + b
print(c)
print(c.count(5) ) # quantas vezes um número aparece dentro de uma tupla