# 아이디어는 해당 계단을 가는데 얼마나 많은 점수를 획득할 수 있는지 이다
# https://daimhada.tistory.com/181 참조

import sys
sys.setrecursionlimit(1000001)


def Solve(stairs,n):
    dp = []
    # 1,2,3 까지의 계단까지 가는데 최대 점수
    dp.append(stairs[0]);
    if n >= 2:
        dp.append(stairs[0]+stairs[1])
    if n >= 3:
        dp.append(max(dp[0]+stairs[2],stairs[1]+stairs[2]))
    if n > 3:
        # 나머지 계단을 가는데 최대 점수
        for i in range(3,n):
            dp.append(max(dp[i-3]+stairs[i-1]+stairs[i],dp[i-2]+stairs[i]))

    return print(dp[-1])

def Input():
    stair = []
    n = int(input())
    for _ in range(n):
        stair.append(int(input()))
    return stair,n


stairs,number = Input()
Solve(stairs,number)
