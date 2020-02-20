
n,m = map(int,input().split())
adj = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    adj[y].append(x)

result = 0

for index in range(1,n+1):
    count = 0
    queue = list()
    queue.append(index)
    while queue:
        next1 = queue.pop(0)
        if len(adj[next1]) == 0:
            result = count
        else:
            for index1 in adj[next1]:
                queue.append(index1)
                count += 1
        print(queue)


