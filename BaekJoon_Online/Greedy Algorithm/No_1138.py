N = int(input())
peoples = list(map(int, input().split()))
result = [0 for _ in range(10)]

for i in range(N):
    count = 0

    for j in range(N):
        # 해당 자리에 아무도 안서있고, 앞에 서있는 사람 수(count)와 peoples의 값이 일치할 경우 자리에 세운다.
        if count == peoples[i] and result[j] == 0:
            result[j] = i + 1
            break

        if result[j] == 0:
            count += 1

for i in range(N):
    print(result[i], end=" ")
print()

"""
# 시간초과 뜬다....
import itertools
import sys

def Check(test):
    check = [0]*N
    for i in range(N):
        count = 0
        for j in range(i,-1,-1):
            if test[i] < test[j]:
                count += 1
        check[test[i] - 1] = count
    return check

N = int(input())
want = list(map(int,input().split()))
mylist = [i+1 for i in range(N)]
mypermuatation =  itertools.permutations(mylist)
for i in mypermuatation:
    check = Check(i)
    if check == want:
        print(*i,sep=' ')
        sys.exit()
"""