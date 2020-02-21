N, X = map(int,input().split())
data = list(map(int,input().split()))
result = []
for index in data:
    if X > index:
        print(index, end=' ')