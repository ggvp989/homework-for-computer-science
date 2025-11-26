#sort
class Node:
    def __init__(self, data, next=None):
        self.data = data;
        self.next = next;

def filter_linked_list(head, predicate_function):
    new_head = None;
    new_tail = None;

    current = head
    while current:
        if predicate_function(current.data):
            new_node = Node(current.data)
            if not new_head:
                new_head = new_node;
                new_tail = new_node;
            else:
                new_tail.next = new_node;
                new_tail = new_node;
        current = current.next;

    return new_head;

# Define a linked list: 1 -> 2 -> 3
original_list = Node(1, Node(2, Node(3)))

# Define a predicate function: x => x >= 2
def predicate_function(x):
    return x >= 2

# Apply the filter method
filtered_list = filter_linked_list(original_list, predicate_function)

# Print the result
current = filtered_list
while current:
    print(current.data, end=" -> ")
    current = current.next
# Output: 2 -> 3 ->
