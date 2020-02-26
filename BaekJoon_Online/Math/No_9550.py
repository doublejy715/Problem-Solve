T = int(input())

for _ in range(T):
    N,K = map(int,input().split())
    data = list(map(int, input().split()))
    result = 0
    for index in range(N):
        result += data[index]//K
    print(result)

"""
더 빠른 코드
import sys
input = sys.stdin.readline
for i in range(int(input())):
    n, k = map(int, input().split())
    print(sum([int(i) // k for i in input().split()]))
"""