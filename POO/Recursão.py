# Recursão é um metódo de resolução de problemas, que divide problemas em problemas menores e menores, até chegar em um problema que possa ser resolvido

# Exemplo 1: somar uma lista;
# 1° maneira

def listaSoma(lista):
    contador = 0
    for i in lista:
        contador = contador + i
    return contador

print(listaSoma([1,3,5,7,9]))

#2° maneira, usando recursão

def soma(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + soma(numlist[1:])
    
print(soma([1,3,5,7,9]))

# Converter em string
def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base,base) + convertString[n%base]

print(toStr(1453,16))
