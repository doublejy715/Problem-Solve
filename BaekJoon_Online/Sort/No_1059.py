import sys

N = int(input())
datas = sorted(list(map(int,input().split())))
check = int(input())
count = 0
for index in range(len(datas)-1):
    if index == 0 and check < datas[index]:
        print((datas[0]-check)*check-1)
        sys.exit()

    elif datas[index] < check < datas[index+1]:
        print((check-datas[index])*(datas[index+1]-check)-1)
        sys.exit()
print(0)
