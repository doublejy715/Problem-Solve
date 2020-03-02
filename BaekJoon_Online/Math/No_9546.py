N = int(input())
data = [0 for _ in range(30)]
data[0] = 1
for i in range(1,30):
    data[i] = data[i-1] + 2**i
for _ in range(N):
    num = int(input())
    print(data[num-1])