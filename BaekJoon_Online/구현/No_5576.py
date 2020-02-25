W = [int(input()) for _ in range(10)]
K = [int(input()) for _ in range(10)]
W.sort(reverse=True)
K.sort(reverse=True)
print(sum(W[:3]), sum(K[:3]))