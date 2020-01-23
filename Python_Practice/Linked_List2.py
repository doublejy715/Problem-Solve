# 객체지향 프로그래밍으로 링크드 리스트 구현하기
#노드의 형성


class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next


# 추가 및, 개체 확인을 위한 class
class NodeMgmt:
    def __init__(self,data): # 기본적으로 시작하자마자 노드를 하나 만든다. 이 노드는 최초의 노드가 된다(헤드)
        self.head = Node(data) # NodeMgmt의 head변수에 최초의 노드를 저장한다.
        # 이렇게 되면 head안에는 추가적으로 data, next의 값을 가지게 된다.(head.data, head.next)

    def add(self,data):
        if self.head == '': # 만약에 head가 존재하지 않을 시에 방어 코드로 이용
            self.head = Node(data)

        else:
            node = self.head
            while node.next: # 마지막 노드를 찾아낸다.
                node = node.next
            node.next = Node(data) # 해당 노드의 다음 값을 새로운 node를 생성해서 지정해 놓는다.

    def desc(self): # 현재의 node를 모두 출력한다.
        node = self.head
        while node: # node가 존재하지 않을때까지 계속해서 출력한다.
            print(node.data)
            node = node.next

    def delete(self,data): # 원하는 데이터를 가진 node를 삭제하는 과정
        # case1. 만약 헤더가 삭제되는경우 -> 기존의 헤더를 삭제하고 새로운 헤더를 지정해 준다.
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        # case2. Linked_List 내부의 node가 삭제 대상일 때
        else:
            node = self.head # 원하는 node.data를  찾기 위해서 헤더부터 찾는다.
            while node.next: # 원하는 데이터를 가진 노드를 전부 훑는다.
                # 원하는 데이터를 찾은 경우
                if node.next.data == data: # 이전의 node값이 필요하므로 미리 찾는 코드 입력
                    node.next = node.next.next # 다다음의 node랑 현재의 node를 이어준다.
                    return
                # 원하는 데이터를 찾지 못한 경우 다음으로 넘긴다.
                else:
                    node = node.next

    #특정 data를 가진 node를 찾아보기
    def search_node(self,data):
        node = self.head
        while node.data:
            if node.data == data:
                return node
            else:
                node = node.next


# test
test_list = NodeMgmt(1) # 이것으로 기본적 헤드 설정
test_list.desc()
for index in range(2,10):
    test_list.add(index)
test_list.delete(4)
test_list.desc()
print(test_list.search_node(8).data)