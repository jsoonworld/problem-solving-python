class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

def get_linked_list_sum(linked_list_1, linked_list_2):
    def linked_list_to_number(linked_list):
        cur = linked_list.head
        result = ""
        while cur is not None:
            result += str(cur.data)
            cur = cur.next
        return int(result)

    num1 = linked_list_to_number(linked_list_1)
    num2 = linked_list_to_number(linked_list_2)
    return num1 + num2



linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))