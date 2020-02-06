test_case = int(input())
data = list()

for i in range(test_case):
    data.append(int(input()))

for index1 in range(test_case):
    min_index = index1
    for index2 in range(index1+1,test_case):
        if data[index2] < data[min_index]:
            min_index = index2
    data[index1],data[min_index] = data[min_index],data[index1]

for i in range(test_case):
    print(data[i])

'''
for i in range(test_case):
    data.append(int(input()))

data.sort()
for i in range(test_case):
    print(data[i])

'''


