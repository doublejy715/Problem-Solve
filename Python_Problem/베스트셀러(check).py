sell = dict()
N = int(input())
for i in range(N):
    Book = input()
    if Book not in sell:
        sell[Book] = 1
    else:
        sell[Book] += 1

sell = dict(sorted(sell.items()))
sell = sorted(sell.items(),key = (lambda x:x[1]), reverse = True )
print(sell[0][0])


'''
sorted 는 값을 정렬 한 후에 반환까지 한다. 기존의 함수에 영향을 미치지 않는다. 반환한 값을 따로 저장해야 된다.
https://www.codeit.kr/questions/186 참조

list.sort는 단순하게 정렬 만 하고 반환은 하지 않는다. 반환하면 None 된다. list에서만 사용 가능하다.
'''
'''
lambda x:x[1]

def f1(x):
    return x[1]

0,1 을 통해서  keys, values 기준을 정할 수 있다.
하는 것과 같다. 해당 자리수를 반환한다.(해당 자리를 기준으로 정렬하게 된다.)
'''