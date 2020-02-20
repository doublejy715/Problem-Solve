import sys
# 함수들
# Cal_A
def Cal_A(maps):
    min_line = 5001
    for i in maps[1:]:
        cal = sum(i)
        if min_line > cal:
            min_line = cal
    return min_line

# Turn
def Turn(maps,x,y,s):
    for index1 in range(1,s+1):
        tmp = maps[x-index1][y-index1]
        #한칸씩 옮긴다.
        for index2 in range(s*2+1):
            if index2 == 0:
                continue
            maps[x-index1+index2-1][y-index1] = maps[x-index1+index2][y-index1]

        for index2 in range(s*2+1):
            if index2 == 0:
                continue
            maps[x-index1+index2-1][y+index1] = maps[x-index1+index2][y+index1]

        for index2 in range(s*2+1):
            if index2 == 0:
                continue
            maps[x+index1][y+index1-index2+1] = maps[x+index1][y+index1-index2]

        for index2 in range(s*2+1):
            if index2 == 0:
                continue
            elif index2 == (s*2+1):
                maps[x + index1 - index2][y - index1] = tmp
            else:
                maps[x+index1-index2+1][y-index1] = maps[x+index1-index2][y-index1]
    return maps

# input
n,m,k = map(int,sys.stdin.readline().split())
maps = [[0 for i in range(m+1)] for j in range(n+1)]
middle = list()
x = 1
for _ in range(n):
    data = list(map(int,sys.stdin.readline().split()))
    for i in range(len(data)):
        maps[x][i+1] = data[i]
    x += 1

for _ in range(k):
    r,c,s = map(int,sys.stdin.readline().split())
    Turn(maps,r,c,s)
    print(maps)


print(Cal_A(maps))


