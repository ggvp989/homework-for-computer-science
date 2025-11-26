#приоритетная очередь
class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def push(self, item, priority):
        self.elements.append((priority, item))
        i = len(self.elements) - 1
        while i > 0 and self.elements[i - 1][0] > self.elements[i][0]:
            self.elements[i - 1], self.elements[i] = self.elements[i], self.elements[i - 1]
            i -= 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty priority queue")
        priority, item = self.elements.pop(0)
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty priority queue")
        return self.elements[0][1]

    def size(self):
        return len(self.elements)
        
pq = PriorityQueue()

pq.push("Задача 1", priority=2)
pq.push("Задача 2", priority=5)
pq.push("Задача 3", priority=1)

print("Первый элемент с наивысшим приоритетом:", pq.peek())  # Ожидаемый вывод: Задача 3

while not pq.is_empty():
    print("Обработка:", pq.pop())
