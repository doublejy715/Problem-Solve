N = int(input())
num = 0
L = 0
data = list(map(int,input().split(' ')))
data.sort()

for _ in range(N):
    if data[_] > num:
        num = data[_]
        L += 1

print(L)