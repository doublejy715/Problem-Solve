import sys

# input
N = sys.stdin.readline()

maps = [0 for _ in range(100001)]
maps[1], maps[2], maps[3] = 3,7,17
for index in range(4,len(maps)):
  maps[index] = maps[index-1]*2 + maps[index-2]

print(maps)
