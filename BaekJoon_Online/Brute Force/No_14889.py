from itertools import combinations,permutations

def Sum(team):
    count = 0
    for i in permutations(team,2):
        count += data[i[0]][i[1]]
    return count


def Input():
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    teams = list(combinations([i for i in range(N)],N//2))

    return N,data,teams

N,data,teams = Input()
result = 10000
for i in range(len(teams)//2):
    power1, power2 = Sum(teams[i]), Sum(teams[len(teams)-i-1])
    result = min(result,abs(power1-power2))

print(result)