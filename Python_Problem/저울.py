N = int(input())
data = list(map(int,input().split()))

ans =0

for i in data:                                      # data의 원소들을 하나씩 가지온다.
    if i <= ans + 1:                                # 만약 이때까지 만든 최소값보다 1더 큰 무게가 data에 존재한다면,
        ans += i                                    # i+ans 까지의 값은 다 만들 수 있다 (일종의 skip)
    else:
        break

print(ans+1)