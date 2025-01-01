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

    def get_kth_node_from_last(self, k):
        # 현재 구현에서는 리스트의 끝에서 K번째를 구하지 않고
        # 처음부터 K번째 값을 반환하려고 함
        # 끝에서 K번째를 찾으려면 리스트 전체 길이나 포인터 조작이 필요
        cur = self.head
        count = 0  # 현재 노드의 인덱스
        flag = True
        while flag:
            if count == k - 1:  # K번째 값과 관련된 조건
                return cur      # 이 조건은 끝에서 K번째를 구하지 않음
            else:
                count += 1
                cur = cur.next  # cur이 None이 되면 에러 발생 가능 (끝을 넘을 경우)
