import sys

data = sys.stdin.readline
N,M = map(int,data().split())
maps = [list(data().strip()) for _ in range(N)]
result = []
count = 0
for j in range(M):
    ch = [['A', 0], ['C', 0], ['G', 0], ['T', 0]]
    for i in range(N):
        for k in range(4):
            if ch[k][0] == maps[i][j]:
                ch[k][1] += 1
    result.extend(max(ch,key= lambda x:x[1])[0])
print(*result,sep='')

index = 0
for j in range(M):
    for i in range(N):
        if result[index] != maps[i][j]:
            count += 1
    index += 1
print(count)

"""
이게 훨씬 더 좋은 코드이다
import sys
In = sys.stdin.readline

def main():
    n, m = map(int, In().split())
    distances = [[0, 0, 0, 0] for _ in range(m)]
    convert = ["A", "C", "G", "T"]
    dic = {"A" : 0, "C" : 1, "G" : 2, "T" : 3}

    for _ in range(n):
        dna = In().rstrip()
        for i, d in enumerate(dna):
            distances[i][dic[d]] += 1 # 여기서 해당 영어의 갯수를 세 준다.(i = 줄 번호)
            
    
    ans = ""
    num = 0
    # 여기서 DNA설계와 H.D.를 알 수 있게 된다.
    for dis in distances:
        max_dis = max(dis)
        ans += convert[dis.index(max_dis)]
        num += sum(dis) - max_dis

    print(ans)
    print(num)
    

main()
"""