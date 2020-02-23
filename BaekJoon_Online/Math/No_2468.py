maps = list(map(int,input().split()))
if maps[2] - maps[1] < maps[1] - maps[0]:
    print(maps[1]-maps[0]-1)
else:
    print(maps[2]-maps[1]-1)