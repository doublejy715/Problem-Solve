N = int(input())
data = [0 for _ in range(13)]
data[0], data[1] = 1,1
for i in range(2,13):
    data[i] = data[i-1]*i
print(data[N])