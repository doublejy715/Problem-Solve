N = int(input())
point = set()
for _ in range(N):
    x1,y1 = map(int,input().split())
    for i in range(x1,x1+10):
        for j in range(y1,y1+10):
            point.add((i,j))
print(len(point))