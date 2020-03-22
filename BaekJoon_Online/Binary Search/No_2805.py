N,M = map(int,input().split())
tree = list(map(int,input().strip().split()))
mini , maxi = 1, max(tree)

while mini <= maxi:
    mid = (mini+maxi)//2

    high = 0
    for i in tree:
        if i - mid >= 0:
            high += i - mid
    if M <= high:
        mini = mid + 1
    else:
        maxi = mid - 1
print(maxi)