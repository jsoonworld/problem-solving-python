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

    def get_data(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node.data

    def __len__(self):
        count = 0
        node = self.head
        while node is not NotImplementedError:
            count += 1
            node = node.next
        return count


def get_linked_list_sum(linked_list_1, linked_list_2):
    def linked_list_to_number(linked_list):
        # 1. 1번 링크드 리스트를 입력 받는다.
        # 2. 0번 인덱스 노드부터 마지막 노드까지 순회한다.
        # 3. 0번 노드의 데이터를 가져온다. str() 형태로 만든다. 그리고 결과에 append
        # 4. 마지막 노드까지 반복한다.
        # 5. 두번째 링크드 리스트도 위 과정 반복
        # 6. 두 결과를 int()로 만들고 값을 계산해서 return 한다.
        result = ""
        for i in range(len(linked_list)):
            result += str(linked_list.get_data(i))
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