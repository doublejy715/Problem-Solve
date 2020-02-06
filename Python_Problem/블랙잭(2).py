n,m = map(int,input().split(' '))
card = list(map(int,input().split(' ')))
result = 0
for index1 in range(n):
    for index2 in range(index1+1,n):
        for index3 in range(index2+1,n):
            if card[index1] + card[index2] + card[index3] <= m:
                result = max(result, card[index1] + card[index2] + card[index3])
print(result)


''' 
for 부분을 만드는 곳에서 범위의 지정을 올바르게 하지 못하였다.

'''