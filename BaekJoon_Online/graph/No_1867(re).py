def dfs(a):
    global v,r,field
    if v[a]:
        return 0
    v[a] = 1
    for b in field[a]:
        if r[b] == -1 or dfs(r[b]):
            r[b] = a
            return 1
    return 0

if __name__ == "__main__":
    # 격자, 돌멩이.
    n, k = map(int, input().split())

    # 운동장.
    field = [[] for i in range(n)]

    # 돌맹이 위치.
    for i in range(k):
        a, b = map(int, input().split())
        field[a - 1].append(b - 1)

    # n 만큼을 돌면서 확인해주면된다.
    v = [0] * n
    r = [-1] * n

    ans = 0
    for i in range(n):
        v = [0] * n
        ans += dfs(i)
    print(ans)