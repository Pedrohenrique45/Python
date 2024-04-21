# quando não sei o limite não posso usar o for, então usar o while
n = 1
while n !=0:
    n = int(input('Digite um valor:'))

print('fim')

# loop infinito com quebra

n = s =0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    s += n 
print(f"a soma vale {s}")
