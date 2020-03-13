num = int(input())
data = list(map(int,input().split()))
data.sort(reverse=True)
count = 0
for i in range(num):
    for j in range(num):
        count += abs(data[i] - data[j])
print(count)