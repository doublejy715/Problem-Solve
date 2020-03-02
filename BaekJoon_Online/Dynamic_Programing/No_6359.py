import sys
N = int(sys.stdin.readline())
for _ in range(N):
    i = int(sys.stdin.readline())
    data = [1 for p in range(i+1)]
    for index in range(2,i+1):
        j = index
        while j < len(data):
            if data[j] == 0:
                data[j] = 1
            else:
                data[j] = 0
            j += index

    print(sum(data)-1)