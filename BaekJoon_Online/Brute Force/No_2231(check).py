import sys

N = int(input())
for i in range(N+1):
    number, lists = str(i), []
    for index in number:
        lists.append(int(index))
    sum1 = sum(lists)
    if sum1 + i == N:
        print(i)
        sys.exit()
print(0)
"""
# 매우 빠른 정답
import math

def numDigit(num):
    return int(math.log(num) / math.log(10)) + 1

def d(a):
#    print (f'The number: {a}' )
    sum = a
    for i in range( numDigit(a)) :
        sum += int(a/(10**i))%10
    return sum

num = int(input())
minCandidate = num - numDigit(num)*9

flag = 0
for j in range( max(1, minCandidate), num):
    if d(j) == num:
        flag = 1
        break

print ( j if flag == 1 else 0 )"""