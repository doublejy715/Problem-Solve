n = int(input())
a = list(map(int, input().split()))
a.sort()

def binary_search(num):
    l = 0
    r = n-1
    while l <= r :
        mid = (l+r)//2
        if a[mid] == num :
            return 1
        elif a[mid] > num :
            r = mid - 1
            # 반 줄여주기 1
        else:
            l = mid + 1
            # 반 줄여주기 2
    return 0

input()
for num in list(map(int, input().split())):
    print(binary_search(num), end = ' ')

"""
# 다른방법 (set의 이용) 탐색 시간복잡도는 O(1)이다.
import sys

input = sys.stdin.readline
n = int(input())
arr = set(map(int,input().split()))
m = int(input())
m_arr= list(map(int,input().split())) 

for i in range(m): 
    if m_arr[i] in arr : 
        print(1,end=' ') 
    else :
        print(0,end=' ')
        
"""
"""
N = int(input())
card = list(map(int,input().split()))
card.sort()

M = int(input())
want = list(map(int,input().split()))
result = [0]*M


for index in range(len(want)):
    start, end = 0, N - 1
    while start <= end:
        mid = (start+end)//2
        if card[mid] == want[index]:
            result[index] = 1
            break
        elif card[mid] > want[index]:
            end = mid - 1
        else:
            start = mid + 1

print(*result,sep=' ')
"""