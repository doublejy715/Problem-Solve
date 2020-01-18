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
            node = self.head             # 현재 헤드에서 맨 앞으로 이동한다.
            while node.next:
                node = node.next
            new = Node(data)             # 새로운 Node를 형성한 뒤 이어준다.
            new.prev = node
            node.next = new
            self.tail = new

    # 3. desc
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    # 4. search from haed
    def search_from_head(self,data):
        node = self.head
        while node:                      # node가 없을때까지 반복한다.
            if node.data == data:
                return node
            else:
                node = node.next
        return False

    # 5. search from tail
    def search_from_tail(self,data):
        node = self.tail
        while node:
            if node.data == data:
                return node
            else:
                node = node.prev
        return False

    # 6. insert_before
    def insert_before(self,data,before_data):   # 매개변수로는 넣을 데이터랑, 어느 앞에 넣을 것인지 확인하는 2개가 필요하다.
        # 일단은 뒤에서 찾아나간 뒤 넣는 작업을 실시 해 준다.
        node = self.tail
        while node.data != before_data:        # 조건문이 만족할 때까지만(True)일 동안에만 반복한다.
            node = node.prev
            if node == None:
                return print(False)
        # 새로운 노드를 생성 및 기존의 노드와 Link를 한다. 새로운 노드의 경로 지정 후 기존 노드를 경로지정한다.
        new_node = Node(data)
        # 6.1 둘 다 된다.
        new_node.next = node
        new_node.prev = node.prev
        node.prev.next = new_node
        node.prev = new_node
        '''
        # 6.2 
        before_new = node.prev
        before_new.next = new_node
        new_node.prev = before_new
        new_node.next = node
        node.prev = new_node
        '''
        return print(True)


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
print()
list.insert_before(5.5,5)
list.insert_before(5.6,5)
list.desc()
