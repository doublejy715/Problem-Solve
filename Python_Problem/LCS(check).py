str1,str2 = input(),input()

data = [[0]*(len(str2)+1) for i in range(len(str1)+1)]

for index1 in range(1,len(str1)+1):
    for index2 in range(1,len(str2)+1):
        if str1[index1-1] != str2[index2-1]:
            data[index1][index2] = max(data[index1][index2-1],data[index1-1][index2])
        else:
            data[index1][index2] = data[index1-1][index2-1] + 1

print(max(data[-1]))

'''
LCS 에 대해서 다시 체크하자
'''