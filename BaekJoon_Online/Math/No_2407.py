# import math 중 factorial 사용 가능
def fact(num):
    if num == 1:
        return 1
    return num*fact(num-1)
N,M=map(int,input().split())
print(fact(N)//(fact(N-M)*fact(M)))