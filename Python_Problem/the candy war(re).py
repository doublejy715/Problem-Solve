T = int(input())

for _ in range(T):
    N = int(input())
    candy = list(map(int,input().split(' ')))
    for index1 in range(len(candy)):
        if candy[index1] % 2 != 0:
            candy[index1] += 1
    count = 0
    result = [0 for i in range(len(candy))]

    while True :
        if max(candy) == min(candy):
            print(0)
            break
        for index2 in range(N):
            if index2 == 0:
                result[index2] = int(candy[-1]/2) + int(candy[index2]/2)
            else:
                result[index2] = int(candy[index2-1]/2) + int(candy[index2]/2)
        candy = result
        for index1 in range(len(candy)):
            if candy[index1] % 2 != 0:
                candy[index1] += 1
        count += 1
    print(count)

