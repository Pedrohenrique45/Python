#Criando uma pilha vazia
def criar_pilha():
    return []

#Chegar se a pilha está vazia
def checar_vazia(pilha):
    return len(pilha) == 0

#Adicionar itens
def push(pilha, item):
    pilha.append(item)
    print(f"Item adicionado: {item}")

#Remover itens
def pop(pilha):
    if (checar_vazia(pilha)):
        return "Pilha vazia"
    return pilha.pop()

pilha = criar_pilha()

push(pilha, 1)
push(pilha, 2)
push(pilha, 3)
push(pilha, 4)
push(pilha, 5)

print(pilha)

pop(pilha)

print(f"Removendo o último item da pilha, {pilha}")