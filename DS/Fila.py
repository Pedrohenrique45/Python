class Queue:        #Criar uma class, para poder construir a fila
    def __init__(self):
        self.queue = []

    # Adicionar um elemento
    def enqueue(self, item):
        self.queue.append(item)

    # Remover um elemento
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # Exibir a fila
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)


q = Queue()  #Instânciar o Objeto
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()

q.dequeue()

print("Depois de remover um elemento")
q.display()