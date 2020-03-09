str1, str2 = map(str,input().split())
if len(str1) < len(str2):
    str1,str2 = str2,str1

count1 = 51
for i in range(len(str1) - len(str2)+1):
    count2 = 0
    for j in range(len(str2)):
        if str1[i+j] != str2[j]:
            count2 += 1
    count1 = min(count1,count2)
print(count1)