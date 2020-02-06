N = int(input())
data = []
sum =0
for _ in range(N):
    data.append(int(input()))

data.sort()
for index in range(1,len(data)+1):
    sum += abs(index - data[index-1])
print(sum)