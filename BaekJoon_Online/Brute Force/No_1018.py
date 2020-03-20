# (0,0)이 W로 반드시 시작하기 때문에 그냥 해당 자리에 W가 맞는지 아닌지 또는 B가 맞는지 아닌지만 확인하면 된다.

def Check(maps,map1,map2):
    count1, count2 = 0, 0
    for i in range(8):
        for j in range(8):
            if map1[i][j] != maps[i][j]:
                count1 += 1
            if map2[i][j] != maps[i][j]:
                count2 += 1
    return min(count1,count2)


def Point(y,x,cheese):
    compare = [[] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            compare[i] += cheese[y+i][x+j]

    return compare

def Make_Cheese():
    map1,map2 = [[] for _ in range(8)],[[] for _ in range(8)]

    for i in range(8):
        for j in range(8):
            if (j+i) % 2 == 1:
                map1[i] += 'W'
                map2[i] += 'B'
            else:
                map1[i] += 'B'
                map2[i] += 'W'

    return map1,map2


def Input():
    N, M = map(int,input().split())
    cheese = [list(input()) for _ in range(N)]
    return N,M,cheese


N,M,cheese = Input()
map1, map2 = Make_Cheese()
result = 64
for i in range(N - 7):
    for j in range(M - 7):
        compare = Point(i,j,cheese)
        result = min(result,Check(compare,map1,map2))

print(result)

"""
# 매우 빠른 버전
import sys
input = sys.stdin.readline

size = 8
def wrongnum(x,y):
  w = 0
  b = 0
  c = ['W','B']
  for i in range(size):
    for j in range(size):
      if board[x+i][y+j] == c[(i+j)%2]:
        w += 1
      else:
        b += 1
  return min(w,b)

N,M = map(int,input().split())
board = []
for _ in range(N):
  board.append(list(input().rstrip()))
sol = []
for x in range(N-size+1):
  for y in range(M-size+1):
    sol.append(wrongnum(x,y))
print(min(sol))
"""