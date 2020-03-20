from itertools import combinations

def Check(data,S):
    count = 0
    for i in range(1,len(data)+1):
        result = list(combinations(data,i))
        for j in range(len(result)):
            sum1 = sum(result[j])
            if sum1 == S:
                count += 1
    return count


def Input():
    N, S = map(int,input().split())
    data = list(map(int,input().split()))
    return N,S,data

N,S,data = Input()
print(Check(data,S))