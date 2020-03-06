data = list(map(int,input().split()))
num = 0
i = min(data)
while True:
    count = 0
    for j in data:
        if i % j == 0:
            count += 1
    if count >= 3:
        print(i)
        break
    i += 1