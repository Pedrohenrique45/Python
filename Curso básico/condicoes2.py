faturamento = 1000
custo = 2000

lucro = faturamento - custo

# tratar varias condições

vendas = int(input("Digite o valor de suas vendas"))
bonus = 0

if vendas >= 15000:
    bonus = 500
elif vendas >= 10000:
    bonus = 150
elif vendas >= 5000:
    bonus = 50
else:
    bonus = 0

print(bonus)

# logica matemática => and/or
# if not => se não...
venda = 17000
vendas_empresa= 60000
meta_empresa = 50000

if vendas >= 15000 and vendas_empresa > meta_empresa:
    bonus = 500
elif vendas >= 10000 and vendas_empresa > meta_empresa:
    bonus = 150
elif vendas >= 5000 and vendas_empresa > meta_empresa:
    bonus = 50
else:
    bonus = 0