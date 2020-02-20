class Node:
    def __init__(self, number, left_node, right_node):
        self.parent = -1
        self.number = number
        self.left_node = left_node
        self.right_node = right_node
def in_order(node, level):
    global level_depth, x
    level_depth = max(level_depth, level)
    if node.left_node != -1:
        in_order(tree[node.left_node], level + 1)
    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    x += 1
    if node.right_node != -1:
        in_order(tree[node.right_node], level + 1)

n = int(input())
tree = {}
level_min = [n]
level_max = [0]
root = -1
x = 1
level_depth = 1
for i in range(1, n + 1):
    tree[i] = Node(i, -1, -1)
    level_min.append(n)
    level_max.append(0)

for _ in range(n):
    number, left_node, right_node = map(int, input().split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node
    if left_node != -1:
        tree[left_node].parent = number
    if right_node != -1:
        tree[right_node].parent = number
for i in range(1, n + 1):
    if tree[i].parent == -1:
        root = i
in_order(tree[root], 1)
result_level = 1
result_width = level_max[1] - level_min[1] + 1
for i in range(2, level_depth + 1):
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i
        result_width = width

print(result_level, result_width)


"""class Node():
    def __init__(self,node_data,left,right):
        self.parrent = -1
        self.node_data = node_data
        self.left = left
        self.right = right

def Mid1(node,level):
    global level_depth, x
    level_depth = max(level_depth, level)
    if node.left != -1:
        Mid1(tree[node.left], level + 1)
    # 중간으로 오면 어떤 일을 해 줘야 하는가?
    level_min[level] = min(level_min[level],x)
    level_max[level] = max(level_max[level],x)
    x += 1
    if node.right != -1:
        Mid1(tree[node.right], level + 1)

node_count = int(input())
tree = {}
level_min = [node_count]
level_max = [0]
root = -1 # 이 문제는 root를 지정해 주지 않는다
x = 1
level_depth = 1


# 초기 설정
for _ in range(1,node_count+1):
    tree[_] = Node(_,-1,-1)
    level_min.append(_)
    level_max.append(0)

# 데이터 입력 받기
for _ in range(1,node_count+1):
    data, left, right = map(int,input().split())
    tree[data].left = left
    tree[data].right = right
    if left != -1:
        tree[left].parrent = data
    if right != -1:
        tree[right].parrent = data

# 부모 노드 지정
for i in range(1,node_count+1):
    if tree[i].parrent == -1:
        root = i

# 트리 순회하면서, 기록하기
Mid1(tree[root],1)

result_level = 1
result_width = level_max[1] - level_min[1] + 1
for i in range(2, level_depth + 1):
    width = level_max[i] - level_min[i] + 1
    if result_width < width:
        result_level = i
        result_width = width

print(result_level, result_width)"""