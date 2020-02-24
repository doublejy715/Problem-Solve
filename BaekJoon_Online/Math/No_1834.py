count, sum = 1,0
N = int(input())
while count < N**2:
    if (count // N) == (count % N):
        sum += count
        count += N
    else:
        count += 1
print(sum)
# 이건 좋은것이 아님 직접 손으로 점화식 푸는게 더 좋음