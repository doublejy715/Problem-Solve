def Turn_Left(maps,find,count):
    while maps[0] != find:
        maps = maps[1:] + [maps[0]]
        count += 1
    return maps,count


def Turn_Right(maps,find,count):
    while maps[0] != find:
        maps = [maps[-1]]+maps[:-1]
        count += 1
    return maps,count


def Turn(maps,find,count):
    while maps[0] != find:
        # Fc.2
        if len(maps)//2 >= maps.index(find):
            maps, count = Turn_Left(maps,find,count)
        # Fc.3
        else:
            maps, count = Turn_Right(maps,find,count)
    maps.pop(0)
    return maps, count


def Input():
    N,M = map(int,input().split())
    maps = list(i+1 for i in range(N))
    want = list(map(int,input().split()))
    return N,M,want,maps



N,M,want,maps = Input()
count = 0
while want:
    maps,count = Turn(maps,want.pop(0),count)
print(count)