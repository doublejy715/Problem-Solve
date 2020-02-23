result = 0
for _ in range(3):
    line = input()
    if _ == 0:
        if line == 'black':
            result += 0
        elif line == 'brown':
            result += 10
        elif line == 'red':
            result += 20
        elif line == 'orange':
            result += 30
        elif line == 'yellow':
            result += 40
        elif line == 'green':
            result += 50
        elif line == 'blue':
            result += 60
        elif line == 'violet':
            result += 70
        elif line == 'grey':
            result += 80
        elif line == 'white':
            result += 90

    elif _ == 1:
        if line == 'black':
            result += 0
        elif line == 'brown':
            result += 1
        elif line == 'red':
            result += 2
        elif line == 'orange':
            result += 3
        elif line == 'yellow':
            result += 4
        elif line == 'green':
            result += 5
        elif line == 'blue':
            result += 6
        elif line == 'violet':
            result += 7
        elif line == 'grey':
            result += 8
        elif line == 'white':
            result += 9

    elif _ == 2:
        if line == 'black':
            result *= 10**0
        elif line == 'brown':
            result *= 10**1
        elif line == 'red':
            result *= 10**2
        elif line == 'orange':
            result *= 10**3
        elif line == 'yellow':
            result *= 10 ** 4
        elif line == 'green':
            result *= 10 ** 5
        elif line == 'blue':
            result *= 10 ** 6
        elif line == 'violet':
            result *= 10 ** 7
        elif line == 'grey':
            result *= 10 ** 8
        elif line == 'white':
            result *= 10 ** 9


print(result)