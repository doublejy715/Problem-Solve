N = int(input())
data = [[1 for _ in range(9)] for _ in range(N)]
data[0][0] = 2

if N == 1:
    print(10)
elif N == 2:
    print(55)
else:
    data[1] = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(2,N):
        for j in range(9):
            if j == 0:
                data[i][j] = sum(data[i-1])
            else:
                data[i][j] = (data[i][j-1] - data[i-1][j-1])%10007
    result = []
    for index in range(len(data)):
        result += data[index]
    print(sum(result)%10007)
