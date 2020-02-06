count = 1
stack = list()
result = list()
n = int(input())
for i in range(1,n+1):
    data = int(input())
    while count <= data:
        stack.append(count)
        result.append('+')
        count += 1
    if data == stack[-1]:
        stack.pop()
        result.append('-')
    else:
        print('No')
        exit(0)

print('\n'.join(result))


'''
count = 1
stack = list()
result = list()
n = int(input())
for i in range(1,n+1):
    data = int(input())
    while count <= data:
        stack.append(count)                     # 원하는 data까지 갈때 해야 될 것
        count += 1
        result.append('+')

    if stack[-1] == data:
        stack.pop()
        result.append('-')
    else:
        print('No')
        exit(0)

print('\n'.join(result))


'''


