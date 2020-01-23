N, M = map(int,input().split(' '))
card = list(map(int,input().split(' ')))

pro = 0
for index1 in range(len(card)):
    for index2 in range(index1,len(card)):
        for index3 in range(index2,len(card)):
            if card[index1] + card[index2] + card[index3] <= M:
                pro = max(card[index1] + card[index2] + card[index3],pro)

print(pro)