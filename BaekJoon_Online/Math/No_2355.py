A, B = map(int,input().split())
big = max(A,B)
small = min(A,B)
if big > small >= 0 :
    print((big+small)*(big-small+1)//2)
elif big >= 0 > small:
    if abs(big) > abs(small):
        print((big-abs(small))*(big+abs(small)+1)//2)
    elif abs(big) == abs(small):
        print(0)
    else:
        print((big-abs(small))*(abs(small)+big+1)//2)
elif big == small:
    print(big)
elif 0 >= big > small:
    print((big+small)*(big-small+1)//2)
"""
더 좋은 코드(시간 소요 짧음)
a,b=map(int,input().split())
if a>b:a,b=b,a
print(b*(b+1)//2-a*(a-1)//2)
"""