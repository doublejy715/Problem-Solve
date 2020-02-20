import sys

# input
test_case = sys.stdin.readline

# DP
data = [0, 1, 2, 4, 0, 0, 0, 0, 0, 0, 0]
for i in range(4, len(data)):
    data[i] = data[i - 1] + data[i - 2] + data[i - 3]

# ouput
for index in range(test_case):
    num = sys.stdin.readline
    print(data[num])
