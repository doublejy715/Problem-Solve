month_day = [0,31,28,31,30,31,30,31,31,30,31,30,31]
week = ['SUN','MON','TUE','WED','THU','FRI','SAT']
month, day = map(int,input().split())
print(week[(sum(month_day[:month]) + day)%7])