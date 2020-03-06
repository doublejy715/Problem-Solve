N = int(input())
maps = [list(map(int,input().split())) for _ in range(N)]
check = [[True]*N for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        for k in range(N):

            if i == j or i == k or k == j:
                continue
            # 만약에 k로 돌아간 것이 그냥 i j 로 간 것과 같다면 그 간선은 없어도 된다.
            elif maps[i][j] == maps[i][k] + maps[k][j]:
                check[i][j] = False

for i in range(N):
    for j in range(N):
        if check[i][j] == True:
            count += maps[i][j]

print(count//2)