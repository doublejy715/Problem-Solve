N,M = int(input()), int(input())
data = list(map(int,input().split()))
count = 0
for i in range(N):
    if M - data[i] in data:
        count += 1
print(count//2)
"""
예외처리를 통한 더 빠른 방법
n = int(input())
m = int(input())

L = list(map(int,input().split()))
d = {}

for i in L:
    d[i] = 1

ans = 0
for i in L:
    k = 0
    try:
        k = d[m-i]
        if i != m-i:
            ans+=1
    except:
        continue
print(ans//2)
"""