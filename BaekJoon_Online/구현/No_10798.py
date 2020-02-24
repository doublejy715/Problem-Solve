data = []
max1 = 0
for i in range(5):
    it = input()
    data.append(it)
    if len(it) > max1:max1 = len(it)
for i in range(5):
    if len(data[i]) != max1:
        for j in range(max1-len(data[i])):data[i] = data[i] + ' '
for index1 in range(len(data[0])):
    for index2 in range(len(data)):
        if data[index2][index1] == ' ': continue
        else: print(data[index2][index1], end='')

"""
예외처리 방식
import sys
r = sys.stdin.readline

read = [r().strip() for _ in range(5)]
max_len = max(read, key=len)             #이것으로 각 list 원소의 최대 길이를 뽑아올 수 있다.

for j in range(len(max_len)):
    for i in range(5):
        try:                            # 예외처리 구간
            print(read[i][j], end="")
        except Exception as e:
            continue
        
"""