data = input()
lists = []
for index in range(len(data)):
    lists.append(data[index:])
print(*sorted(lists),sep='\n')