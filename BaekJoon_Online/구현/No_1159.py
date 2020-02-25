N = int(input())
data = [0 for _ in range(27)]
result = list()
for i in range(N):
    name = input()
    data[ord(name[0])-97] += 1
for index in range(len(data)):
    if data[index] >= 5:
        result.append(chr(index+97))

if len(result) == 0:
    print('PREDAJA')
else:
    print(*result,sep='')