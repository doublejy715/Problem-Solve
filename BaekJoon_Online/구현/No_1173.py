import sys
N, C = map(int,sys.stdin.readline().strip().split())
data = set()
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    for i in range(1,(C//num)+1):
        data.add(i*num)
print(len(data))

"""
이것이 매우 빠름
n,c=map(int,input().split())
t=[0]*(c+1)
for _ in range(n):
    i=int(input())
    for j in range(i,c+1,i):t[j]=1
print(sum(t))
"""