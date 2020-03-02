N = int(input())
A = list(map(int,input().split()))
data = []
for index,x in enumerate(A):
    data.append([index, x])
data.sort(key= lambda x:x[1])
result = [0]*N
for index,x in enumerate(data):
    result[x[0]] = index
print(*result)
