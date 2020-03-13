import sys
from itertools import combinations

def Lotto(num,numbers):
    result = list(map(' '.join, combinations(numbers, 6)))
    print(*result,sep='\n')


def Input():
    data =list(map(str,input().split()))
    if len(data) == 1:
        sys.exit()
    else:
        return data[0], data[1:]

while True:
    num, numbers = Input()
    Lotto(num,numbers)
    print()
