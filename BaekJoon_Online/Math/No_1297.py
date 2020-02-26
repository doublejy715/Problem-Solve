import math
D,H,S = map(int,input().split())
a= ((D**2*H**2/(S**2+H**2))**0.5)
print(math.floor(a),math.floor(a*S/H))