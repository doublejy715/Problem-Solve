

# 노드의 모습을 먼저 만들어본다.
    # node는 자신의 데이터와 다음 node의 위치를 결정짓는다.
class Node:  # node는 여러개 만들어 지므로 class 틀이 낫다.
    def __init__(self,data): # 만들자말자 node를 만들게 한다.
        self.data = data
        self.next = None

# init(형성하자마자), is_empty(비어있는가), push(삽입), pop(추출), peek(엿보기) 의 기능을 가지게 한다.
class stack:
    # 1. init : 하나 stack을 형성하게 되면 아무것도 없다.
    def __init__(self):
        self.head = None # (stack변수).head = (첫번쨰 노드이름) 하면 head 지정 가능
        # stack의 head는 어디인가?

    # 2. is_empty : 비어있는지 여부 -> 헤드의 여부를 확인한다.
    def is_empty(self):
        if not self.head:  # 이런 헝태이면 0인지 아닌지 확인 가능하다.
            return True
        else:
            return False
"""
이런 형태는 안되나?
if len(self) == 0:
    return True
else:
    return False
"""
    #3. push
    def push(self,data):
        new_node = Node(data) # 새로운 노드를 하나 만들어준다.
        new_node.next = self.head
        self.head = new_node.data


# 결국 class Node는 칸을 만들어 나갈 뿐이고, 그것에 대한 역할을 class stack이 부여해 준다.(어느 node가 헤드인지, 끝인지)
# 단순히 class stack은 head,