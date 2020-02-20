data = [0 for _ in range(12)]
data[1],data[2],data[3] = 1, 2, 4
for i in range(4, len(data)):
    data[i] = data[i - 1] + data[i - 2] + data[i - 3]
for index in range(int(input())):
    print(data[int(input())])

"""
import sys
test_case = int(sys.stdin.readline())
data = [1, 2, 4, 0, 0, 0, 0, 0, 0, 0]
for i in range(3, len(data)):
    data[i] = data[i - 1] + data[i - 2] + data[i - 3]
for index in range(test_case):
    num = int(sys.stdin.readline())
    print(data[num-1])
"""
