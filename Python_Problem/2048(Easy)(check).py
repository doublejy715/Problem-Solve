import sys
from copy import deepcopy

sys.setrecursionlimit(100000)

N = int(sys.stdin.readline())
maps = []

def convert(x):


def rotate90(maps):



# 최대값을 나타내어주는 함수이다.
def Bfs(N,maps,count):
    ret = max([max(i)for i in maps])
    if count == 0:
        return ret
    # 판을 돌리기 시작한다.
    for _ in range(4):
        # 먼저 좌측으로 밀어준다.
        # maps을 한 문장씩 받아와서 convert에 넣어준다.
        X = [convert(x) in maps]
        if maps != X:
            ret = max(ret, Bfs(N,X,count-1))
        maps = rotate90(maps)
    return ret



for _ in range(N):
    maps.append(list(map(int,sys.stdin.readline().split())))



print(Bfs(N,maps,5))