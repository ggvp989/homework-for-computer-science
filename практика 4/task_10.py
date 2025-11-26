#двусвязный список
class Node:
    def __init__(self, data):
        self.data = data;
        self.next = None;
        self.prev = None;
class DoublyLinkedList:
    def __init__(self):
        self.head = None;
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return;
        cur = self.head;
        while cur.next:
            cur = cur.next
        cur.next = new_node;
        new_node.prev = cur;
    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return;
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node;
    def delete(self, data):
        if self.head is None:
            return;
        cur = self.head;
        if cur.data == data:
            self.head = cur.next;
            if self.head:
                self.head.prev = None;
            return;
        while cur and cur.data != data:
            cur = cur.next;
        if cur is None:
            return;
        if cur.next:
            cur.next.prev = cur.prev;
        if cur.prev:
            cur.prev.next = cur.next;

    def display(self):
        cur = self.head;
        parts = [];
        while cur:
            parts.append(str(cur.data))
            cur = cur.next;
        parts.append("None")
        print(" <-> ".join(parts));
    def display_reverse(self):
        if self.head is None:
            print("None");
            return;
        cur = self.head
        while cur.next:
            cur = cur.next;
        parts = [];
        while cur:
            parts.append(str(cur.data))
            cur = cur.prev
        parts.append("None")
        print(" <-> ".join(parts))

dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.display()
dll.prepend(0)
dll.display()
dll.delete(2)
dll.display()
dll.display_reverse()
