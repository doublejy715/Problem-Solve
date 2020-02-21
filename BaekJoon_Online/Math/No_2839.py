inp = int(input())
Box = 0
while True:
    if (inp % 5) == 0:
        Box = Box + (inp//5)
        print(Box)
        break
    inp = inp-3
    Box += 1
    if inp < 0:
        print("-1")
        break

"""
N = int(input())
bag = 10001
if N % 5:
    bag = N//5
else:
    K5 = N // 5
    for i in range(0,K5+1):
        if (N - i*5)%3 == 0:
            bag = min(bag,i + ((N - i*5)//3))

if bag == 10001:
    print(-1)
else:
    print(bag)
"""