class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Management:
    # 1. __init__ : 노드 하나를 지정해 준다.
    def __init__(self,data):
        self.head = Node(data)

    # 2. Add
    def Add(self,data):
        # 만약 데이터가 없는 경우(처음 삽입)
        if not self.head:
            self.head = Node(data)

        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    # 3. delete
    def Delete(self,data):
        # 경우를 생각해 줘야한다. : 스텍에 데이터가 없을때, 삭제하고자 하는 값이 head일때, 삭제하고자 하는 값이 중간에 존재할때
        # 3.1 스텍에 데이터가 없을때
        if not self.head:
            print("값을 가진 노드가 없습니다.")
            return

        # 3.2 삭제하고자 하는 값이 head일때,
        if self.head.data == data:
            tmp = self.head
            self.head = self.head.next
            del tmp
            return

        # 3.3 삭제하고자 하는 값이 중간에 존재할 때 (check)
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    tmp = node.next
                    node.next = node.next.next
                    del tmp
                    pass
                else:
                    node = node.next

    # 4. search
    def search_node(self,data):
        node = self.head
        while node.next:
            if node.data == data:
                return True
            else:
                node = node.next
        return False

stack = Management(0)
for data in range(1,10):
    stack.Add(data)

print(stack.search_node(5))
print(stack.search_node(11))
stack.Delete(5)
print(stack.search_node(5))