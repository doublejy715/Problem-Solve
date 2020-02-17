import copy

test_case = int(input())
data = list()




for i in range(test_case):
    num = int(input())
    data = list(i+1 for i in range(num))

print(data)

