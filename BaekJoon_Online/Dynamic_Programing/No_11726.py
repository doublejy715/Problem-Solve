import sys
sys.setrecursionlimit(10**6)

N = int(input())
data = [0 for _ in range(N+1)]
data[0], data[1], data[2] = 0,1,2
if N <= 2:
    print(data[N])
else:
    for index in range(3,N+1):
        data[index] = (data[index-2] + data[index -1])%10007
    print(data[N])