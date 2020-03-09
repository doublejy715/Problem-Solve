def recur(idx):
    # 완성 되었는지 검사
    if len(tmp) == k+1:
        result.append(tmp[:])
        return

    for i in range(10):
        # 시작 숫자를 정한다.
        if idx == -1 and candi[i]:
            tmp.append(i)
            candi[i] -= 1
            recur(idx + 1)
            tmp.pop()
            candi[i] += 1
        else:
            # 시작하고나서 부등호를 들고온다.
            if a[idx] == '<':
                # 실제로 부등호와 일치하는지 그리고 쓴 적이 존재하는지 확인한 뒤 조건이 만족하면 tmp에 추가
                if tmp[idx] < i and candi[i]:
                    tmp.append(i)
                    candi[i] -= 1
                    recur(idx+1)
                    tmp.pop()
                    candi[i] += 1
 
            elif a[idx] == '>':
                if tmp[idx] > i and candi[i]:
                    tmp.append(i)
                    candi[i] -= 1
                    recur(idx+1)
                    tmp.pop()
                    candi[i] += 1
 
k = int(input())
a = input().split()
candi = [1]*10
tmp = []
result = []
recur(-1)
print(''.join(map(str, result[-1])))
print(''.join(map(str, result[0])))