def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]        # 부모 집합이 어디에 속해 있는지 보여주는 것

def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

test_case = int(input())

for _ in range(test_case):
    parent = dict()     # 가족을 가리키는 것
    number = dict()     # 멤버가 몇명인지 보는 것

    f = int(input())
    for _ in range(f):
        x, y = input().split(' ')
        # 일단 각각 인원으로 넣어두고 나중에 union한다.
        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        union(x,y)

    print(number[find(x)])