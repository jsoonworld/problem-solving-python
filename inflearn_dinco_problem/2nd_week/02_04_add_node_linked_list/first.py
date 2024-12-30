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

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):
        # 1. get 노드를 호출해서 index 번째 노드를 가져온다.
        # 2 index 번째 노드가 가리키는 next를 추가하려는 노드의 next에 넣는다.
        # 3. index 번째 노드의 next를 새로운 노드 가리키게 연결한다.
        index_node = self.get_node(index)

        new_node = Node(value)
        new_node.next = index_node.next

        index_node.next = new_node



linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.print_all()
