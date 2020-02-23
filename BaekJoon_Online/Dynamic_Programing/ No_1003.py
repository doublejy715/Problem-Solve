list1 = []

test_case = int(input())
for i in range(test_case):
    list1.append(int(input()))
data = [[0,0] for i in range(41)]
data[0] = [1,0]
data[1] = [0,1]

for j in range(2,41):
    data[j][0] = data[j-1][0] + data[j-2][0]
    data[j][1] = data[j-1][1] + data[j-2][1]

for ij in list1:
    for index in range(2):
        if index == 0:
            print(data[ij][index],end=' ')
        else:
            print(data[ij][index])

