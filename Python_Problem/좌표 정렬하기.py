tc = int(input())
data = list()
for _ in range(tc):
    data.append(list(map(int,input().split())))

data.sort(key = lambda x:x[0])
data.sort(key = lambda x:x[1])

for index in range(len(data)):
    print(data[index][0] ,data[index][1])