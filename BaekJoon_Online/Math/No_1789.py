N = int(input())
count = 0
while (count*(count+1))//2 <= N:
    if (count*(count+1))//2 == N:
        count += 1
    else:
        count += 1
print(count-1)

"""
최단시간
print(int(((-1+(1+8*int(input()))**0.5)/2)))
"""