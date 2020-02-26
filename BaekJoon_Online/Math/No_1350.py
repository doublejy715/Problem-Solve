import math
N = int(input())
count = 0
data = list(map(int,input().split()))
store = int(input())
for i in range(N):
    count += math.ceil(data[i]/store)
print(count*store)