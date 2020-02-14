class Node()
    def __init__(self,data,left=None,right=None):
        self.data = data
        self.right = right
        self.left = left

class NodeNgmt():
    # 1. 생성
    def __init__(self,data):
        node = Node(data)
        self.head = node
        self.tail = node

    # 2. insert
    def insert(self, data):

    # 3. insert_before : before_data 앞에다가 삽입
    def insert_bofore(self, data, before_data):
        if not self.head :
            self.head = Node(data)
            return True
        else:
            node = self.head
            while node.data != before_data:
                node = node.left
                if node == None:
                    return False
            


    # 4. insert_after
