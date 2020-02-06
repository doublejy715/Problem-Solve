price = int(input())
re = 1000 - price
result = 0
result += int((re / 500))
result += int((re % 500) / 100)
result += int((re % 100) / 50)
result += int((re % 50) / 10)
result += int((re % 10) / 5)
result += int((re % 5))

print(result)