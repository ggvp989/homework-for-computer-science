#
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None;
class LinkedList:
    def __init__(self):
        self.head = None;
def linked_list(*values):
    linked_list = LinkedList()
    if not values:
        return linked_list;
    linked_list.head = Node(values[0])
    current = linked_list.head;
    for value in values[1:]:
        current.next = Node(value)
        current = current.next;
    return linked_list;
def print_linked_list(linked_list):
    current = linked_list.head
    while current:
        print(current.value, end=" -> ");
        current = current.next
    print("None");
def get_node_and_prev(linked_list, index):
    if not linked_list.head:
        return None, None;
    if index == 0:
        return linked_list.head, None;
    current = linked_list.head
    prev = None
    count = 0
    while current and count < index:
        prev = current
        current = current.next
        count += 1
    if count != index or not current:
        return None, None;
    return current, prev;
def swap_nodes(list_pointer1, index1, list_pointer2, index2):
    list1 = list_pointer1[0];
    list2 = list_pointer2[0];
    node1, prev1 = get_node_and_prev(list1, index1);
    node2, prev2 = get_node_and_prev(list2, index2);
    if not node1 or not node2:
        return False;
    if prev1:
        prev1.next = node2
    else:
        list1.head = node2
    if prev2:
        prev2.next = node1
    else:
        list2.head = node1;

    node1_next = node1.next
    node2_next = node2.next

    node1.next = node2_next
    node2.next = node1_next

    return True;
  
# Example usage
list1 = linked_list(1, 2, 3, 4)
list2 = linked_list(5, 6, 7, 8)

result = swap_nodes([list1], 2, [list2], 0)
print(result)  # Output: True

print_linked_list(list1)
# Output: 1 -> 2 -> 5 -> 4 -> None

print_linked_list(list2)
# Output: 3 -> 6 -> 7 -> 8 -> None

list1 = linked_list(1, 2, 3)
list2 = linked_list(4, 5, 6)

result = swap_nodes([list1], 1, [list2], 3)
print(result)  # Output: False

print_linked_list(list1)
# Output: 1 -> 2 -> 3 -> None

print_linked_list(list2)
# Output: 4 -> 5 -> 6 -> None
