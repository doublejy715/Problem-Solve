test_case = int(input())

for _ in range(test_case):
    left = []
    right = []
    data = input()
    for i in data:
        if i == '-':
            if left:
                left.pop()
        elif i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        else:
            left.append(i)
    left.extend(reversed(right))
    print(''.join(left))
'''
for i in range(test_case):
    data = list(input())
    left = list()
    right = list()
    for index in range(len(data)):
        if data[index] == '<':
            if len(left) != 0:
                right.append(left.pop(-1))
        elif data[index] == '>':
            if len(right) != 0:
                left.append(right.pop(-1))
        elif data[index] == '-':
            if len(left) != 0:
                left.pop(-1)
        else:
            left.append(data[index])
    print(left+right)

'''

