n = int(input())
sum = 0
for i in range(n):
    if i == 0:
        sum += 5
    elif i == 1:
        sum += 7
    else:
        sum += 7+3*(i-1)
print(sum%45678)
# 좋지 못함 다른 점화식 존재