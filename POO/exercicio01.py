class Cliente:
    def __init__(self, nome,email, plano):
        self.nome = nome
        self.email = email
        self.lista_planos = ['basic', 'premium']
        if plano in self.lista_planos:
            self.plano = plano
        else:
            raise Exception('Plano invalido')
        pass

    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_planos:
            self.plano = novo_plano
        else:
            print("plano invalido")
        pass

    def ver_filme(self, filme, plano_filmme):
        if self.plano in plano_filmme:
            print(f'ver filme {filme}')
        elif self.plano == "premiun":
            print(f'ver filme {filme}')
        elif self.plano == "basic" and plano_filmme == "premium":
            print(f'faça upgrde para ver esse filme :{filme}')
        else: 
            print('plano invalido')

        pass


cliente = Cliente("Pedro", "papaosdomcos@gmail.com", "basic")
print(cliente.plano)
cliente.mudar_plano("prsk")
print(cliente.plano)