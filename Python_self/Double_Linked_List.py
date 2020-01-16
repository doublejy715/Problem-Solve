'''
double linked list 는 다음과 같은 기능을 가진다.
1. 노드형성 2.insert 3. desc 4.search from head 5.search from tail 6.insert_before
'''

# 1. Node
class Node():
    # 앞뒤로 노드가 이어져 있는 구조이므로 매개변수가 3개 필요하다.
    def __init__(self,data,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class Double_Linked_List():
    # 클래스가 가지는 기본적인 변수는 head, tail 이다. 만들어짐과 동시에 head와 tail의 값은 같다
    def __init__(self,data):
        self.head = Node(data)
        self.tail = self.head

    # 2. insert
    def insert(self,data):
        # 2.1 만약 list에 아무것도 없다면?
        if self.head == '':
            self.head = Node(data)
            self.tail = self.head
        # 2.2 list에 데이터가 있어 이어주는 경우
        else:
            node = self.head        # 현재 헤드에서 맨 앞으로 이동한다.
            while node.next:
                node = node.next
            new = Node(data)        # 새로운 Node를 형성한 뒤 이어준다.
            new.prev = node
            node.next = new
            self.tail = new

    # 3. desc
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

list = Double_Linked_List(0)
list.insert(3)
list.insert(4)
list.insert(5)
list.insert(6)
list.insert(7)

print(list.head.data)
print(list.tail.data)
print()
list.desc()
