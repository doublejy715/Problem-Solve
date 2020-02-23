data = []
for _ in range(3):
    data.append(list(map(int,input().split())))
for i in data:
    if sum(i) == 0:
        print('D')
    elif sum(i) == 1:
        print('C')
    elif sum(i) == 2:
        print('B')
    elif sum(i) == 3:
        print('A')
    else:
        print('E')