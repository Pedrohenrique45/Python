faturamento = 1000
custo = 700

lucro = faturamento - custo

print(f'Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}')

# pode também contatenar com '+'

email = 'emailfalso@gmail.com'

print(email.lower()) # coloca o email todo em letra minuscula

print(email.find("@")) # procura algo especifico no texto 

print(email[1])

# pegar pedaços de textos

posicao = email.find("@")
servidor = email[posicao:]
print(servidor)

#tamanho de um texto
tamanho = len(email)
print(tamanho)

#trocar um pedaço do texto

email_trocado = email.replace("gmail.com", "hotmail.com")
print(email_trocado)

# editar nome

nome = "pedro henrique"
print(nome.capitalize()) #Pedro henrique
print(nome.title()) #pedro Henrique

#especiais, transformar número em texto

print(f'Faturamento: {faturamento:,.2f}, Custo: {custo}, Lucro: {lucro}')

#exercicios
nome = "Pedro Henrique"
email = 'pmailfalso2@gmail.com'

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


# Construa uma mensagem: "Enviamos um link para de confirmação para o email j****@gmail.com"

mensagem = f'Enviamos um link de confirmação para o email {email[0]}*****{servidor}'
print(mensagem)