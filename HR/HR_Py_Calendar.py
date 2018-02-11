import calendar

# print(calendar.TextCalendar(firstweekday=6).formatyear(2018))
print(list(calendar.day_name)[calendar.weekday(2015, 8, 5)])

l = list(map(int, input().split()))
print(list(calendar.day_name)[calendar.weekday(l[2], l[0], l[1])].upper())
