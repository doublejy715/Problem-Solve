A,B = input().split()
AMIN,AMAX,BMIN,BMAX = A.replace("6","5"),A.replace("5","6"),B.replace("6","5"),B.replace("5","6")
print(int(AMIN)+int(BMIN), int(BMAX) + int(AMAX),sep=' ')