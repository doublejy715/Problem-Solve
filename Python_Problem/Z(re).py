def sol(lens,x,y):
    if lens == 2:
        if x == X and y == Y:
            print(result)
            return
        result += 1
        if x == X and y + 1 == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y == Y:
            print(result)
            return
        result += 1
        if x + 1 == X and y+1 == Y:
            print(result)
            return
        result += 1
        return
    sol(lens/2,x,y)
    sol(lens/2,x,y+N/2)
    sol(lens/2,x+N/2,y)
    sol(lens/2,x+N/2,y+N/2)

global result
N,X,Y = map(int,input().split(' '))
sol(2**N,0,0)
        