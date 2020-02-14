# 이진 탐색(삽입, 삭제)
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    # 시작하자마자 root node 지정
    def __init__(self, head):
        self.head = head

    # 1. Insert
    def Insert(self, value):
        self.current_node = self.head
        # 재귀호출이 아닌 while의 무한 호출로 형성되어 있다.
        while True:
            # 1.1 value가 현재 data값 보다 작은경우
            if value < self.current_node.value:
                if not self.current_node.left == None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break

            # 1.2 value가 현재 data값 보다 큰 경우
            else:
                if not self.current_node.right == None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    # 2. search
    def search(self, value):
        self.current_node = self.head
        while True:
            # 2.1 현재 값이 찾으려는 값보다 큰 경우
            if value < self.current_node.value:
                # 노드의 존재 여부 확인(다음 노드를 위함)
                if self.current_node.left == None:
                    return False
                else:
                    self.current_node = self.current_node.left
            # 2.2 현재 값이 찾으려는 값보다 작은 경우
            elif value > self.current_node.value:
                if self.current_node.right == None:
                    return False
                else:
                    self.current_node = self.current_node.right
            # 2.3 현재 값이 찾으려는 값이랑 일치하는 경우
            elif value == self.current_node.value:
                return True

    # 3. delete
    def Delete(self, value):
        # 3.1 value를 가진 노드가 존재하는지 확인(동시에 parrent_node, current_node 바로 지정)
        searched = False
        self.current_node = self.head
        self.parrent_node = self.head
        while True:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parrent_node = self.current_node
                self.current_node = self.current_node.left
            elif value > self.current_node.value:
                self.parrent_node = self.current_node
                self.current_node = self.current_node.right
        if not searched:
            return False

        # 3.2 자식노드가 없는 경우
        if self.current_node.right == None and self.current_node.left == None:  # 이거 if not self.current_node.right 되는가?
            if self.parrent_node.value < value:
                self.parrent_node.right = None
            else:
                self.parrent_node.left = None
            del self.current_node

        # 3.3 자식노드가 1개인 경우(오른쪽, 왼쪽의 구분)
        if self.current_node.right == None and self.current_node.left != None:
            if self.parrent_node.value > value:
                # 그런데 이거 parrent_node.left가 없을때는 가능한데 만약 존재하게 되면 어떻게? -> 이런 경우는 존재하지 않는다. 자식노드가 크거나 작아도 어차핀 정렬되어 있는 것이기 때문에 기존의 체계를 무너뜨리는 일은 없다.
                self.parrent_node.left = self.current_node.left
            else:
                self.parrent_node.right = self.current_node.left

        elif self.current_node.right != None and self.current_node.left == None:
            if self.parrent_nodel.value < value:
                self.parrent_node.right = self.current_node.right
            else:
                self.parrent_node.left = self.current_node.right

        # 3.4 자식노드가 2개인 경우(추가 해야됨)
        elif self.current_node.right != None and self.current_node.left != None:
