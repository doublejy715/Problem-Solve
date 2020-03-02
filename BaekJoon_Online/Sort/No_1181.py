import sys

N = int(sys.stdin.readline())
data = [ sys.stdin.readline().strip() for _ in range(N)]
leght = [[] for _ in range(51)]
for index,x in enumerate(data):
    if x in leght[len(x)]:
        continue
    leght[len(x)].append(x)

for i in range(len(leght)):
    leght[i].sort()

for i in range(len(leght)):
    if not leght[i]:
        continue
    else:
        print(*leght[i],sep='\n')


"""
이게 훨씬 더 빠르다
import sys
n = int(sys.stdin.readline())
arr = []
for i in range(n):
  arr.append(sys.stdin.readline().strip())
arr = list(set(arr)) # 나도 시도해 봤는데 왜 안됬는지 모르겠다.
# 1. 첫번째 글자 기준으로 한번 정렬 2. 단어 길이를 기준으로 정렬
arr2 = sorted(sorted(arr), key = lambda x: len(x)) # lambda의 다양한 이용, 길이를 기준으로 한 정렬
l = len(arr2)
print('\n'.join(arr2))
"""
