import math
N = int(input())
for _ in range(N):
    N,M = map(int,input().split())
    print(int(math.factorial(M)/(math.factorial(N)*math.factorial(M-N))))

"""
# 이 코드가 시간 덜걸리고 메모리도 적게 사용한다.
# 1
import sys

def Fact(num):
    if num <= 1:
        return 1
    return num*Fact(num-1)

N = int(sys.stdin.readline().strip())
for _ in range(N):
    N,M = map(int,sys.stdin.readline().strip().split())
    print(int(Fact(M)/(Fact(N)*Fact(M-N))))

# 2 (가장 짧게 걸린다.)
import sys
import math
N = int(sys.stdin.readline().strip())
for _ in range(N):
    N,M = map(int,sys.stdin.readline().strip().split())
    print(int(math.factorial(M)/(math.factorial(N)*math.factorial(M-N))))
"""