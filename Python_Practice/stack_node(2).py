# Node : 데이터를 저장할 공간이다.
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# stack
class stack:
    # 1. __init__ : 처음 시작할시 head는 None 표현
    def __init__(self):
        self.head = None

    # 2. Isempty
    def Isempty(self):
        if not self.head:
            return True
        else:
            return False

    # 3. Push
    def Push(self,data):
        # 과정 : 새로운 노드 형성, 새 노드의 next를 다음 노드 지정, 현재 스택의 head 최신화
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 4. Pop
    def Pop(self):
        # 과정 : 현제 최상위 노드 추출, 최상위 노드 다음 것을 head로 최신화, return
        if self.Isempty():
            return None
        tmp = self.head
        self.head = self.head.next
        return tmp

    # 5. Top
    def Top(self):
        if self.Isempty():
            return None
        return self.head.data

q = stack()
print(q.Isempty())
q.Push(1)
q.Push(2)
q.Push(3)
q.Push(4)
print(q.Isempty())
print(q.Top())
print(q.Pop())
print(q.Top())
print(q.Pop())
