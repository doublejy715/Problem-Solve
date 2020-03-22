import sys
from itertools import permutations

cal = 0
N = sorted(list(input()),reverse=True)
for i in N:
    cal += ord(i) - 48

if '0' not in N or cal %3 != 0:
    print(-1)
    sys.exit()
else:
    for i in permutations(N,len(N)):
        number = int(''.join(i))
        if number % 30 == 0:
            print(number)
            sys.exit()
