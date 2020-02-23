A,B,V = map(int,input().split())
if V <= A:
    print(1)
else:
    print((V-A-1)//(A-B)+2)
"""
왜 틀렸지?
A,B,V = map(int,input().split())
days = 0
high = 0
while high != V:
    if high == 0:
        high += A
    else:
        high -= B
        high += A
    days += 1
print(days)
"""