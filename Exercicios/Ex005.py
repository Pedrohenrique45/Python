#Defina uma classe que possua pelo menos dois métodos: getString: para obter uma string da entrada do console printString: para imprimir a string em maiúsculas. Inclua também uma função de teste simples para testar os métodos de classe.

class pegarString(object):
    def __init__(self):
        self.s = ""
        pass

    def getString(self):
        self.s = input("Digite uma palavra: ")

    def printString(self):
        print(self.s.upper())

    
objeto = pegarString()
objeto.getString()
objeto.printString()