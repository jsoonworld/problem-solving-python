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
        # count 를 0으로 만든다.
        # index와 현재의 count 값이 같다면 현재 노드를 반환한다.
        # 만약 다르다면 현재 위치를 다음 노드로 이동시키고 count를 증가시킨다.
        count = 0
        cur = self.head
        while cur == None:
            if count == index:
                return cur.data
            cur = cur.next
            count += 1

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.get_node(0) # -> 5를 들고 있는 노드를 반환해야 합니다!