class MyCircularQueue:
    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    # Inserir um elemento na fila circular
    def enqueue(self, data):
        if (self.tail + 1) % self.k == self.head:
            print("A fila circular está cheia\n")
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = data

    # Remover um elemento da fila circular
    def dequeue(self):
        if self.head == -1:
            print("A fila circular está vazia\n")
        elif self.head == self.tail:
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return temp

    def printCQueue(self):
        if self.head == -1:
            print("Nenhum elemento na fila circular")
        elif self.tail >= self.head:
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


# Seu objeto MyCircularQueue será instanciado e chamado da seguinte forma:
obj = MyCircularQueue(5)
obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Fila inicial")
obj.printCQueue()

obj.dequeue()
print("Depois de remover um elemento da fila")
obj.printCQueue()
