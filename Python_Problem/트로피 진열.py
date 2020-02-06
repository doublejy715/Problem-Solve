N = int(input())
DP = list()

def count(DP):
    max1 = 0
    count1 = 0
    for i in range(len(DP)):
        if DP[i] > max1:
            count1 += 1
            max1 = DP[i]
        else:
            continue
    return count1

def reverse_count(DP):
    max2 = 0
    count2 = 0
    for i in range(len(DP)-1,-1,-1):
        if DP[i] > max2:
            count2 += 1
            max2 = DP[i]
        else:
            continue
    return count2

# 입력 받기
for j in range(N):
    DP.append(int(input()))


print(count(DP))
DP.reverse()                # DP.reservse 로 간단하게 할 수 있다.
print(count(DP))            # print(reverse_count(DP)