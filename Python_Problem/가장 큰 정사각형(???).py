# input
N, M = map(int,input().split(' '))
A = [[0 for _ in range(M+1)] for i in range(N+1)]                       # for _ in range() 앞에 존재하는 형태를 반복해 준다.
    # DP[i][j]는 점이 i,j 칸에 왔을때 만들어지는 최대 정사각형의 크기
    # DP 점화식 : DP[i][j] = min(DP[i-1][j], DP[i-1][j-1], DP[i][j-1]) + 1(?????)
DP = [[0 for _ in range(M+1)] for i in range(N+1)]

for i in range(N):
    for idx, j in enumerate(list(map(int,list(input())))):              # input()의 str를 리스트 형태로 만들면 각 원소들을 리스트 안에 담아준다.
        A[i+1][idx+1] = j                                               # enumerate는 index와 값을 동시에 반환해 준다. (index, values 형식)
        # 위에서는 enumerate로 구분된 idx, j 를 A(데이터)에 넣어준다.


# solve
for i in range(1, N+1):
    for j in range(1, N + 1):
        if A[i][j]:
            DP[i][j] = min(DP[i - 1][j], DP[i - 1][j - 1], DP[i][j - 1]) + 1
            mx = max(DP[i][j], mx)
print(mx)

