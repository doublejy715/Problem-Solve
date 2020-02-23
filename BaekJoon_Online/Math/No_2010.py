import sys

N = int(sys.stdin.readline())
result = 0
for _ in range(N):
    if _ == 0:
        result += int(sys.stdin.readline())
    else:
        result -= 1
        result += int(sys.stdin.readline())
print(result)