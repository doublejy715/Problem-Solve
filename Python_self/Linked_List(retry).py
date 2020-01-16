'''
Linked List
Linked List 는 기본적으로 이전노드를 잇는 데이터를 가진 노드들의 합이다.
1.Node 2.append 3.delete 4.desc(값 모두 출력하기) 5.Search_Node
'''

# 1. Node
class Node():
    def __init__(self,data,next=None):   # 노드는 기본적으로 Linked_List 클래스 내부에서 사용된다.
        self.data = data
        self.next = next

# Linked List class의 형성
class Linked_List_Class():
    # Linked_List의 형성 : head를 가장 먼저 설정해 준다.
    def __init__(self,data):
        self.head = Node(data)

    # 2. append
    def append(self,data):
        # 2.1 linked list에 데이터가 하나도 존재하지 않을때
        if self.head == None:
            self.head = Node(data)

        # 2.2 linked list에 데이터가 하나 이상 존재할 때
        else:
            new_node = Node(data)       # 새로운 노드의 형성
            new_node.next = self.head   # 새로운 노드의 next는 현재 head가 된다.
            self.head = new_node.data   # 새로운 노드를 이어줬으므로 head를 바꿔준다.

    # 3. delete
    def delete(self,data):
        # delete는 3가지 경우로 나뉘어진다. 헤더가 없을때, 헤더가 삭제될떄, linked list의 중간값이 삭제될떄
        # 3.1 헤더가 존재하지 않을떄(?)
        if self.head=='':
            return print("해당 값을 가진 노드가 없습니다.")

        # 3.2 헤더가 삭제될때
        elif self.head.data == data:
            del_node = self.head
            self.head = self.head.next
            del del_node

        # 3.3 linked list의 중간값이 삭제될 때
        else:
            tmp = self.head             # head로부터 원하는 값이 있는곳까지 이동한다.
            while tmp.data == data:     # 원하는 data의 전후 노드가 pre_tmp, tmp로 저장된다.
                pre_tmp = tmp
                tmp = tmp.next
            pre_tmp.next = tmp.data

    # 4. desc
    def desc(self):
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next


test = Linked_List_Class(int(0))
test.append(int(1))
test.append(int(2))
test.append(int(3))
test.desc()



