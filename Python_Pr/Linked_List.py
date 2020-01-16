# 연습 Node의 정의
class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

node1 = Node(1)
head = node1

# Linked_list의 추가 함수 정의
def add(data):
    node = head  # head에서 시작해서 none이 나올때까지 반복한다.(마지막 node까지 진행한다.)
    while node.next:
        node = node.next
    node.next = Node(data)  # 마지막 node까지 이동 후 추가하는 Node class를 이용하여 다음 주소로 등록시킨다.(동시에 node추가 생성)

# Node의 연결
node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1 # 검색을 위해서 가장 앞의 노드를 알아놓는다

# Linked_list 반복 생성
for index in range(2,10):
    add(index)
# Linked_list 출력하기
'''
node = node1
while node.next:
    print(node.data)
    node = node.next
print(node.data)
'''
# 1,2 node 사이에 1.5의 값을 가진 node를 넣어보기
# 1.5의 data를 가진 node를 형성한다.
node3 = Node(1.5)

#먼저 넣고자 하는 node data=1인 것 부터 찾는다.
node = head
search = True
# 원하는 결과가 아니면 계속해서 넘겨준다
while search:
    if node.data == 1:
        search = False
    else:
        node = node.next
# 원하는 곳에서 멈췄다(이 다음 노드가 어떤 이름인지 모르므로 node.next를 통해 임의로 지정하여준다.
node_next=node.next # 임의로 저장하기 위해서 변수를 하나 만들어준다.
node.next = node3 # 찾은 노드에서 끼워 넣을 노드를 지정해 준다.
node3.next = node_next # 끼워 넣을 노드에서 다음 노드 주소를 지정하여 준다.

node = node1
while node.next:
    print(node.data)
    node = node.next
print(node.data)
