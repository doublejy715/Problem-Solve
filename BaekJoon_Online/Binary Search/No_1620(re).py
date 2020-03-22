import sys
input = sys.stdin.readline
import operator
 
def findStr(x) :  
    
    s = 0
    l = n-1
 
    while True :             
        ptr = (l + s) // 2        
        if s_pdic[ptr][1] == x :
            break
        elif s_pdic[ptr][1] < x :
            s = ptr + 1
        else :
            l = ptr - 1           
    return ptr
 
n, m = map(int, input().split())
 
pdic = {}
 
for i in range(n) :
    pdic[i] = input().rstrip()
 
s_pdic = sorted(pdic.items(), key=operator.itemgetter(1))
 
for i in range(m) :
 
    tmp = input().rstrip()
    
    if tmp.isdigit() :
        print(pdic.get(int(tmp)-1))
    else :            
        print(s_pdic[int(findStr(tmp))][0]+1)