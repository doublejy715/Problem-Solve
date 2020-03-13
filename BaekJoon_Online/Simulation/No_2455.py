data = [list(map(int,input().split())) for _ in range(4)]
max1,count = 0, 0
for m,p in data:
    count = count + p - m
    max1 = max(max1,count)
print(max1)