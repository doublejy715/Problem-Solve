import sys
n, T = map(int,sys.stdin.readline().strip().split())
tlist = list(map(int,sys.stdin.readline().strip().split()))
for index in range(len(tlist)):
    T -= tlist[index]
    if T < 0:
        print(index)
        break
    if index == (len(tlist)-1) and T >= 0:
        print(n)