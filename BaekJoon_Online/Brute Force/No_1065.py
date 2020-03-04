data = [111,123,135,147,159,210,222,234,246,258,321,333,345,357,369,420,432,444,456,468,531,543,555,567,579,630,642,654,666,678,741,753,765,777,789,840,852,864,876,888,951,963,975,987,999]

N = input()
if len(N) <= 2:
    print(N)
else:
    count = 99
    for i in data:
        if int(N) >= i:
            count += 1
    print(count)

"""
N = int(input())
count = 0
for i in range(1,N+1):
    if i < 100:
        count += 1
    else:
        data = list(map(int,str(i)))
        if data[0] - data[1] == data[1] - data[2]:
            count += 1

print(count)

"""