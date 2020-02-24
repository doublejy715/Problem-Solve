import sys
N,M = map(int,sys.stdin.readline().split())

hear = set(sys.stdin.readline().strip()for _ in range(N))
face = set(sys.stdin.readline().strip()for _ in range(M))
hear_face = sorted(list(hear & face))
print(len(hear_face))
print(*hear_face, sep="\n")

"""
위에것이 더 우수한 성적이다.
N,M = map(int,input().split())
hear = set(input() for _ in range(N))
face = set(input() for _ in range(M))
hear_face = sorted(list(hear & face))

print(len(hear_face), *hear_face, sep="\n")
"""

