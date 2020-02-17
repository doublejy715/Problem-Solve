test_case = int(input())

for _ in range(test_case):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(i, idx) for idx, i in enumerate(queue)]
    print(max(queue, key= lambda x:x[0]))
    count = 0
    while True:
        if queue[0][0] == max(queue, key= lambda x:x[0])[0]:
            count += 1
            if queue[0][1] == m:
                break
            else:
                queue.pop(0)
        else:
            queue.append(queue.pop(0))