n,m = map(int,input().split(' '))
data = []

for index1 in range(n):
    team,mem_num = input(),int(input())
    member = list()
    for index2 in range(mem_num):
        member.append(input())
    data.append([team,member])

list1 = []
for index3 in range(m):
    ask,how = input(),int(input())
    list1.append([ask, how])

for index4 in range(len(list1)):
    if list1[index4][1] == 1:
        for index5 in range(n):
            if data[index5][1] in list1[index4][0]:
                print(data[index5][0])
    else:
        for index5 in range(n):
            if data[index5][0] is list1[index4][0]:
                for index6 in range(len(data[index5][1])):
                    print(data[index5][1])

