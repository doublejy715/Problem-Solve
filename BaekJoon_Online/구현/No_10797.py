num = int(input())
cars = list(map(int,input().split()))
result = 0
for i in cars:
    if num == i:
        result += 1
print(result)