N = int(input())
card = list(map(int,input().split()))
cards = dict()
card.sort()
for index in card:
    if index not in cards:
        cards[index] = 1
    else:
        cards[index] += 1

M = int(input())
want = list(map(int,input().split()))
result = [0]*M

for index in range(len(want)):
    start, end = 0, N - 1
    while start <= end:
        mid = (start+end)//2
        if card[mid] == want[index]:
            result[index] = cards[want[index]]
            break
        elif card[mid] > want[index]:
            end = mid - 1
        else:
            start = mid + 1

print(*result,sep=' ')

"""
# 코테계의 적폐 파이썬
from collections import Counter
#입력
n = int(input())
nums = Counter(list(map(int, input().split())))
m = int(input())
search = list(map(int, input().split()))
# 출력
for num in search:
    print(nums[num], end=' ')
"""