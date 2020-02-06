class Node():
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

def mid(node):
    print(node.data, end='')
    if node.left != '.':
        mid(tree[node.left])
    if node.right != '.':
        mid(tree[node.right])


def left1(node):
    if node.left != '.':
        left1(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        left1(tree[node.right])


def right1(node):
    if node.left != '.':
        right1(tree[node.left])
    if node.right != '.':
        right1(tree[node.right])
    print(node.data, end='')

N = int(input())
tree = dict()
for _ in range(N):
    data, left, right = map(str,input().split(' '))
    tree[data] = Node(data,left,right)

mid(tree['A'])
print()
left1(tree['A'])
print()
right1(tree['A'])






'''
# 노드의 형성
class Node():
    def __init__(self, data_node, left_node, right_node):
        self.data_node = data_node
        self.left_node = left_node
        self.right_node = right_node

# 좌우가 . 인 부분에서 멈추도록한다.
def mid(node):
    print(node.data_node, end=' ')
    if node.left_node != '.':
        mid(tree[node.left_node])
    if node.right_node != '.':
        mid(tree[node.right_node])

def left1(node):
    if node.left_node != '.':
        left1(tree[node.left_node])
    print(node.data_node, end=' ')
    if node.right_node != '.':
        left1(tree[node.right_node])

def right1(node):
    if node.left_node != '.':
        right1(tree[node.left_node])
    if node.right_node != '.':
        right1(tree[node.right_node])
    print(node.data_node, end=' ')


# 트리의 형성
N = int(input())
tree = {}                   # dict으로 지정해 준다. 해당 data가 가지고 있는 정보를 key로 두고 위치 정보 넣어준다.
for i in range(N):
    data, left, right = map(str,input().split(' '))
    tree[data] = Node(data,left,right)

mid(tree['A'])
print()
right(tree['A'])
print()
left(tree['A'])

'''