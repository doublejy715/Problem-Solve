data = [0 for _ in range(10)]
A = int(input())
B = int(input())
C = int(input())
num = list(str(A*B*C))
for i in num:
    data[int(i)] += 1
for j in data:
    print(j)
