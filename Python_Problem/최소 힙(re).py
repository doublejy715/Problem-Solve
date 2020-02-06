N = int(input())
list1 = list()
data = list()
for i in range(N):
    data1 = int(input())
    if data1 == 0 and len(data) == 0:
        print(0)
    elif data1 == 0 and len(data) != 0:
        print(data[-1])
        data.pop()
    elif data1 != 0:
        data.append(data1)