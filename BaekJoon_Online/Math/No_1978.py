import sys

N = sys.stdin.readline()
list1 = list(map(int,sys.stdin.readline().split()))
count1 = 0
result = []
for index1 in list1:
    if index1 == 1:
        continue
    count2 = 0
    for index2 in range(1,index1+1):
        if not index1%index2:
            count2 += 1
    if count2 == 2:
        count1 += 1

print(count1)