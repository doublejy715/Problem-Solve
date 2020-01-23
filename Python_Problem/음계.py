data = list()
data = input().split(' ')
data = list(map(int,data))              # data의 내부 형식을 int로 바꾸고 반복적으로 한 뒤에 list 형식으로 바꾼다.
'''
ascend = 0
descend = 0
for index in range(1,len(data)):
    if data[index] == data[index-1] + 1:
        ascend += 1
    elif data[index] == data[index-1] - 1:
        descend += 1

if ascend == 7:
    print('ascending')

elif descend == 7:
    print('descending')
else:
    print('mixed')
'''

ascend = True
descend = True
mix = True
for index in range(1,len(data)):
    if data[index] != data[index-1] + 1:
        ascend = False
    elif data[index] != data[index-1] - 1:
        descend = False

if ascend == True:
    print('ascending')

elif descend == True:
    print('descending')
else:
    print('mixed')