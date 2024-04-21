galera = list()
dado = list()
totmai = totmen = 0

for c in range(0,3):
    galera.append(str(input('Nome: ')))
    dado.append(str(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

print(galera)

for p  in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade ')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1

print(f"{totmai} maiores e {totmen} menores de idadde")