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

    # def get_kth_node_from_last(self, k):
    #     cur = self.head
    #     length = 0
    #
    #     while cur:
    #         length += 1
    #         cur = cur.next
    #
    #     target_index = length - k
    #     if target_index < 0:
    #         return None
    #
    #     cur = self.head
    #     for _ in range(target_index):
    #         cur = cur.next
    #
    #     return cur

    def get_kth_node_from_last(self, k):
        cur = self.head
        length = 0

        while cur:
            length += 1
            cur = cur.next

        target_index = length - k
        if target_index < 0:
            return None

        cur = self.head
        for i in range(target_index):
            cur = cur.next

        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!