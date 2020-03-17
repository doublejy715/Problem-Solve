import sys
read = sys.stdin.readline

N = int(read())
data = dict()
for _ in range(N):
    num = int(read())
    if not num in data:
        data[num] = 1
    elif num in data:
        data[num] += 1

for i in sorted(data):
    if max(data.values()) == data[i]:
        print(i)
        break