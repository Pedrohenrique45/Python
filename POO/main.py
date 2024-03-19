# Primeira parte criamos objetos e na segunda parte usamos classes
# no python classe é a mesma coisa que um objeto

class ControleRemoto:
    #carcteristicas
        #cor, altura profundidade, largura 
    #métodos - verbos
    #Primeira coisa que fazemos ao criar uma classe é criar a função init(inicializar a classe)
    #Todos os atributos tem que está no Init
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura

        #self é o próprio controle remoto
        pass
    def passar_canal(self, botao):
        if botao == "+":
            print("aumentar o canal")
        elif botao == "-":
            print("dimminuir o canal")



controle_remoto = ControleRemoto("Preto", "10cm", "2cm", "2cm")
#atributos
print(controle_remoto.cor)
print(controle_remoto.altura)
print(controle_remoto.profundidade)
print(controle_remoto.largura)

#Metodo
controle_remoto.passar_canal("+")

controle_remoto2 = ControleRemoto('cinza', '20cm', '1cm', '2cm')
#Atributos
print(controle_remoto2.cor)
print(controle_remoto2.altura)
print(controle_remoto2.profundidade)
print(controle_remoto2.largura)

#Metodo
controle_remoto2.passar_canal("-")

