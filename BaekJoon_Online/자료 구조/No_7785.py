import sys

input = sys.stdin.readline
N = int(input())
lists = set()
for i in range(N):
    name, status = input().strip().split()
    if status == 'enter':
        lists.add(name)
    else:
        lists.remove(name)
print(*sorted(lists,reverse=True),sep='\n')
