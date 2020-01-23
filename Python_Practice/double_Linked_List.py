
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data=data
        self.next=next
        self.prev=prev


# 추가 및, 개체 확인을 위한 class
class NodeMgmt:
    def __init__(self,data): # 기본적으로 시작하자마자 노드를 하나 만든다. 이 노드는 최초의 노드가 된다(헤드)
        self.head = Node(data) # 헤드를 바로 저장한다.
        self.tail = self.head # 처음 만들었으므로 자기 자신이 꼬리가 된다.

    # case1 : 자료 현황
    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    # case2 : 맨 뒤에 삽입하는 경우
    def insert(self,data):
        if self.head == None:  # head가 지정되어있지 않는 경우
            self.head = Node(data)
            self.tail = self.head
        else:  # head가 존재하여 앞에서 찾기 시작
            node = self.head
            while node.next:
                node = node.next
            new = Node(data)
            node.next = new  # 새로 생긴 노드를 이어준다.
            new.prev = node  # 새로 생긴 노드를 이전의 노드와 이어준다.
            self.tail = new  # 자신의 tail을 새로 생긴 노드로 지정한다.

    # case3 : 맨 앞에서 찾는 경우
    def front_from_head(self,data):
        node = self.head
        while node.next:
            if node.data == data:
                return node
            else:
                node = node.next

    # case4 : 맨 뒤에서 찾는 경우
    def front_from_tail(self,data):
        node = self.tail
        while node.prev:
            if node.data == data:
                return node
            else:
                node = node.prev
    # case5 : 특정 데이터를 찾은 뒤에 해당 노드 '앞'에 새로운 노드를 삽입하는 경우



    
    def insert_before(self,data,defore_data): # data:넣고자 하는 data, defore_data : 앞에 넣고자하는 목표 data
        node = self.tail
        while node.data != defore_data: # 원하는 위치를 찾는다.
            node = node.prev
        new = Node(data)
        new.next = node
        new = node.prev
        node.prev.next = new
        node.prev = new
