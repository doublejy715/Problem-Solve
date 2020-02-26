data= [(1967,'DavidBowie'),(1969,'SpaceOddity'),(1970,'TheManWhoSoldTheWorld'),(1971,'HunkyDory'),(1972,'TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars'),(1973,'AladdinSane'),(1973,'PinUps'),(1974,'DiamondDogs'),(1975,'YoungAmericans'),(1976,'StationToStation'),(1977,'Low')\
       ,(1977,'Heroes'),(1979,'Lodger'),(1980,'ScaryMonstersAndSuperCreeps'),(1983,'LetsDance'),(1984,'Tonight'),(1987,'NeverLetMeDown'),(1993,'BlackTieWhiteNoise'),(1995,'1.Outside'),(1997,'Earthling'),(1999,'Hours'),(2002,'Heathen'),(2003,'Reality'),(2013,'TheNextDay'),(2016,'BlackStar')]
N = int(input())

for _ in range(N):
    Y1,Y2 = map(int,input().split())
    count = 0
    result = list()
    for index in range(len(data)):
        if Y1 <= data[index][0] <= Y2:
            count += 1
            result.append(data[index])
    print(count)
    for i in range(len(result)):
        print(*result[i],sep=' ')

"""
더 센스있는 방법
import sys
readline = sys.stdin.readline
def readint():
    return int(readline())
def readints():
    return list(map(int, readline().rstrip().split()))
def readnints(n):
    return [readint() for _ in range(n)]

album = """
1967 DavidBowie
1969 SpaceOddity
1970 TheManWhoSoldTheWorld
1971 HunkyDory
1972 TheRiseAndFallOfZiggyStardustAndTheSpidersFromMars
1973 AladdinSane
1973 PinUps
1974 DiamondDogs
1975 YoungAmericans
1976 StationToStation
1977 Low
1977 Heroes
1979 Lodger
1980 ScaryMonstersAndSuperCreeps
1983 LetsDance
1984 Tonight
1987 NeverLetMeDown
1993 BlackTieWhiteNoise
1995 1.Outside
1997 Earthling
1999 Hours
2002 Heathen
2003 Reality
2013 TheNextDay
2016 BlackStar
""".strip()
album = [a.split() for a in album.split('\n')]

Q = readint()
for q in range(Q):
    S, E = readints()
    r = []
    for a in album:
        if S <= int(a[0]) <= E:
            r.append(a)
    print(len(r))
    for a in r:
        print(' '.join(a))
"""