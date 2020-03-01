N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
data.sort(key = lambda x:x[0])
data.sort(key = lambda x:x[1])
for i in range(N):
    print(*data[i],sep=' ')

"""
이게 더 빠르다
import sys

N = int(sys.stdin.readline())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
data.sort(key = lambda x:(x[1],x[0]))
for i in range(N):
    print(*data[i],sep=' ')
"""