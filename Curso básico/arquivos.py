# função open() abre um arquivo

#arquivo = open("Vendas.txt", "r")

# fazer oq quiser com o arquivo

#arquivo.close()

with open("vendas.txt", "r") as arquivo:
    infos = arquivo.readlines()

vendas_totais = 0
for item in infos:
    item = item.replace("\n", "")
    item = item.replace(" ", " ")
    resultado = item.split(",")
    valor = resultado[1]
    valor = float(valor)
    print(resultado[1])

print(vendas_totais)