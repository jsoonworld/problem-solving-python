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
        # 현재 위치 노드의 값을 출력한다.
        # 현재 노드가 가리키는 다음 노드가 존재하는지 확인한다.
        # 있다면 현재 위치를 다음 노드로 이동시킨다.
        print(self.head.data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            print(cur.data)


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.print_all()