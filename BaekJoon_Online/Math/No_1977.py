import math
a = int(input())
b = int(input())
c = list()
for i in range(a,b+1):
    print(math.sqrt(i))
    print(int(math.sqrt(i)))
    if math.sqrt(i) == int(math.sqrt(i)):
        c.append(i)

if len(c) == 0:
    print("-1")

else:
    print(sum(c))
    print(min(c))

"""
# for 문이 2개이기 때문에 시간이 너무 오래 걸린다. 
M = int(input())
N = int(input())
data = []
for index in range(M,N+1):
    for i in range(1,index):
        if i*i==index:
            data.append(index)
if len(data) == 0:
    print(-1)
else:
    print(sum(data))
    print(min(data))
"""