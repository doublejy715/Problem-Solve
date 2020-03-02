import sys

N = int(sys.stdin.readline())
for _ in range(N):
    num1, num2 = map(int,sys.stdin.readline().strip().split())
    print(num1+num2)