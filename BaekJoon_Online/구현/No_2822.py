data = []
sum1 = 0
for i in range(8):
    score = int(input())
    data.append([i+1,score])
data.sort(key = lambda x:x[1])
data = data[3:]
data.sort(key = lambda x:x[0])
for i in range(5):
    sum1 += data[i][1]
print(sum1)
for i in range(5):
    print(data[i][0],end=' ')
    