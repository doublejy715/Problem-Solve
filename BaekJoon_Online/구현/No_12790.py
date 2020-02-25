N = int(input())
for i in range(N):
    HP, MP, att, deff, eHP, eMP, eatt, edeff = map(int,input().split())
    if HP+eHP <= 0:
        num1 = 1
    else:
        num1 = HP+eHP
    if MP+eMP <= 0:
        num2 = 5
    else:
        num2 = 5 * (MP + eMP)
    if (att+eatt) <= 0:
        num3 = 0
    else:
        num3 = 2*(att+eatt)
    num4 = 2*(deff+edeff)
    print(num1+num2+num3+num4)
"""
이게 더 좋음
import sys

num = int(sys.stdin.readline())
for i in range(num):
	nlist = [int(x) for x in sys.stdin.readline().split()]
	hp = nlist[0] + nlist[4]
	if hp < 1:
		hp = 1
	mp = nlist[1] + nlist[5]
	if mp < 1:
		mp = 1
	attack = nlist[2] + nlist[6]
	if attack < 0:
		attack = 0
	defense = nlist[3] + nlist[7]
	print(hp + 5*mp + 2*attack + 2*defense)
"""