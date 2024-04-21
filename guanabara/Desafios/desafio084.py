# criar duas listas
# criar um while para cadastro
# depois somar as pessoas 
#criar um lista com pessoas leves e pesadas
temp = list()
princ = list()
mai =  men = 0
while True:
    temp.append(input('Nome: '))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        elif temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    continuar = input("Quer continuar? (S e N) ")
    if continuar in 'Nn':
        break

print('-=' * 30)
print(f"O total de pessoas cadastradas foram {len(princ)}")
print(f'O maior peso foi de {mai}Kg. Peso de', end='')
for p in princ:
    if p[1] == mai:
        print(f"[{p[0]}]", end= '')
print()
print(f"O menor peso foi de {men}Kg", end='')
for p in princ:
    if p[1] == men:
        print(f" [{p[0]}]", end='')
print()




    



