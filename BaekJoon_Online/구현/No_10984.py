Test = int(input())
for i in range(Test):
    N = int(input())
    num, score = 0, 0
    for index in range(N):
        C, G = map(float,input().split())
        num += C
        score += G*C
    print(int(num),round(score/num,1),sep=' ')