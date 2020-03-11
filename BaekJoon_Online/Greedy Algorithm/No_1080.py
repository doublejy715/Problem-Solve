# https://mizzo-dev.tistory.com/entry/baekjoon1080 의 풀이 과정 참조
# 서로 두개의 맵을 비교해서 다르면 계속해서 바꿔준다. 각 위치마다 보고 달라서 바꿨는데 서로 다르면 실패하게 된다.
import sys
"""
# A,B의 값이 서로 다르면, 뒤집어주기 시작한ㄷ나.
def flip(x, y, A):
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            A[i][j] = 1 - A[i][j]


N, M = map(int, input().split())
A, B, result = [], [], 0

for _ in range(N):
    A.append(list(map(int, list(input()))))

for _ in range(N):
    B.append(list(map(int, list(input()))))

for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            result += 1
            flip(i + 1, j + 1, A)


for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            print(-1)
            exit()

print(result)"""

# but runtime Error 발생 // 아마 for문이 너무 많아서 그렇게 된 것 같음 -> for문 줄여서 해
def Reverse(i,j):
    for yy in range(3):
        for xx in range(3):
            if maps1[i + yy][j + xx]:
                maps1[i + yy][j + xx] = 0
            else:
                maps1[i + yy][j + xx] = 1

y,x = map(int,input().split())
maps1 = [list(map(int,input())) for _ in range(y)]
maps2 = [list(map(int,input())) for _ in range(y)]
count = 0

for i in range(y-2):
    for j in range(x-2):
        if maps1[i][j] != maps2[i][j]:
            count += 1
            Reverse(i,j)

for i in range(y):
    for j in range(x):
        if maps1[i][j] != maps2[i][j]:
            print(-1)
            sys.exit()
print(count)
