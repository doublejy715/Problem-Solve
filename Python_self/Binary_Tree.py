'''
트리는 변수를 head를 가진다 root node이다.
기본적으로 이진트리는 링크드 리스트로 형성 할 수 있다.
기본적으로 노드 형성 클래스와 트리 클래스로 나누어서 생각한다.
1. class node
    data, left, right
2. class tree
    insert
    search(종류 : DLR)
    delete
'''

class Node():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class tree():
    def __init__(self,head):
        self.head = head

    # 1. insert
    def insert(self,data):
        self.current_node = self.head                        # 시작할 위치를 지정해 놓는다.
        while True:                                          # 해당 조건이 만족할 동안만 작동한다.
            # 값의 크기를 비교해서 넣어준다.
            # 1.1 삽입하려는 값이 현재의 값보다 작은 경우.
            if self.current_node.value > data:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(data)
                    break
            # 1.2 삽입하려는 값이 현재의 값보다 큰 경우
            elif self.current_node.value < data:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(data)
                    break

    # 2. search
    def search(self,data):
        self.current_node = self.head
        while self.current_node.data:
            # 2.1 찾는 값이 일치하는 경우
            if self.current_node == data:
                return True
            # 2.2 찾는 값이 현재 노드보다 더 큰 경우
            elif self.current_node > data:
                self.current_node = self.current_node.right
            # 2.3 찾는 값이 현재 노드보다 더 작은 경우
            else:
                self.current_node = self.current_node.left

        # 찾지 못하는 경우
        return False

head = Node(2)
BST = tree(head)
BST.insert(1)
BST.insert(3)
BST.search(1)