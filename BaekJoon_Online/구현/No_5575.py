for _ in range(3):
    h1,m1,s1,h2,m2,s2 = map(int,input().split())
    if s1 > s2:
        m2 -= 1
        s2 += 60
    rs = s2 - s1

    if m1 > m2:
        h2 -= 1
        m2 += 60
    rm = m2 - m1
    rh = h2 - h1
    print(rh,rm,rs,sep=' ')