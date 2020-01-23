# Node를 형성하면 자기자신의 값을 가진 Node를 만들어 낸다. 찍어낼 필요가 있으므로 class이
class Node:
    def __init__(self,value): # 변수는 왼쪽 오른쪽 주소값, 자기 자신의 값을 가진다.
        self.value = value
        self.left=None
        self.right=None

# Tree를 관리하기 위한 코드를 만들어 낸다.
class NodeMgmt:
    # head의 설정
    def __init__(self,head): # 트리를 형성하자마자 head로 만들어지는 것을 head root로 자동 지정하여 준다.
        self.head = head

    # 삽입하는 과정
    def insert(self,value):
        # head부터 차례대로 값의 크기를 비교해 나간다.
        self.current_node = self.head
        while True :
            # 만약 들어온 값이 현재 노드값보다 작은 경우
            if self.current_node.value > value:
                # 만약 왼족에 값이 존재한다면?
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                # 만약 왼쪽에 값이 존재하지 않는다면 노드를 새로 하나 생성하여 준다.
                else:
                    self.current_node.left = Node(value)
                    break
            # 만약 들어온 값이 현재 노드값보다 큰 경우
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break
        # 반복하면 적합한 위치로 이동하여 Node를 생성하게 된다.
    # Tree에 존재하는 Node들 중에서 원하는 value가 있는지 검색하여 주는 정의
    def search(self,value):
        self.current_node = self.head
        while self.current_node:
            # 찾고자 하는 값이 있는 경우
            if self.current_node.value == value:
                return True
            # 찾고자 하는 값이 현재 Node값보다 큰 경우
            elif self.current_node.value < value:
                self.current_node = self.current_node.right
            # 작은 경우
            else:
                self.current_node = self.current_node.left
        return False

    # 노드를 삭제하기 위한 정의
    def delete(self,value):
        # 먼저 삭제하기 위한 node의 위치를 찾아나간다.
        searched = False
        # 처음 시작할때는 두 변수다 head로 지정하여 준다.
        self.current_node = self.head # 현재 노드의 위치를 알려준다.
        self.parrent = self.head # 현재 노드의 parrent를 저장하여 준다.
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            # current_node의 위치가 변하게 되면 parrent_node의 위치 또한 변경해 줘야한다.
            elif self.current_node.value < value:
                self.parrent = self.current_node
                self.current_node = self.current_node.right
            else:
                self.parrent = self.current_node
                self.current_node = self.current_node.left
        # 형재 삭제할 노드의 위치를 찾은 상황이다.
        # case1 : 삭제할 노드의 자식노드가 존재하지 않는 경우
        if self.current_node.left == None and self.current_node.right == None
            if self.parrent.left > value:
                self.parrent.left = None
            else:
                self.parrent.right = None
            del self.current_node

        # case2 : 삭제할 노드의 자식노드가 한개 존재하는 경우
        # 삭제할 노드의 자식노드가 왼쪽에 존재하는 경우
        if self.current_node.left != None and self.current_node.right == None:
            # 부모 노드에 새롭게 달아준다.
            if value < self.parrent.value:
                self.parrent.left = self.current_node.left
            else:
                self.parrent.right = self.current_node.left
        # 삭제할 노드의 자식노드가 오른쪽에 존재하는 경우
        elif self.current_node.left == None and self.current_node.right != None:
            # 부모 노드에 새롭게 달아준다.
            if value < self.parrent.value:
                self.parrent.left = self.current_node.left
            else:
                self.parrent.right = self.current_node.left

        # case3 : 삭제할 노드의 자식노드가 양쪽에 존재하는 경우
        # case3의 경우는 여러 변수가 필요하다. 삭제할 노드의 부모노드, 자식노드 중에서 가장 작은 것을 찾기 위한 과정이 있다.
        else:
            self.change_node = self.current_node.right
            self.change_node_parrent = self.current_node.right
            while self.change_node_node:
                if self.chagne_node != None:
                    


