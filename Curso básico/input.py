nome = input("Digite aqui seu nome: ")
email = input('Digite aqui seu email: ')

# Descubra o servidor do email
posicao = email.find("@")
servidor = email[posicao:] # : é ate o final
print("O servidor é: ",servidor)

# Pegar o 1° nome do usuario

nome =  nome.split()
print('Seu primeiro nome é: ',nome[0])

# posicao = nome.find(" ")
# primeiro_nome = nome[:posicao]
# print(primeiro_nome)

# Construa uma mensagem "usuario Pedro Henrique Cadastrado com sucesso com o email..."

print(f'Usuário, {nome[0]} Cadastrado com sucesso com o email: {email}')

