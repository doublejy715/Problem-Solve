E,S,M = map(int,input().split())
if E==15:
    E = 0
if S == 28:
    S = 0
if M == 19:
    M = 0
count = 1
while True:
    if count%15 == E and S==count%28 and M==count%19:
        break
    else:
        count += 1

print(count)
