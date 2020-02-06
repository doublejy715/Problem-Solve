N = int(input())
CR = list(map(int,input().split(' ')))
M = int(input())
box = list(map(int,input().split(' ')))
CR.sort(reverse=True)
box.sort(reverse=True)
count = 0


if CR[0] < box[0]:
    print(-1)
else:
    while len(box) != 0:
       for index2 in range(len(box)):
            for index1 in range(len(CR)):
                if CR[index1] >= box[index2]:
                    del box[index2]
            count += 1

print(count)