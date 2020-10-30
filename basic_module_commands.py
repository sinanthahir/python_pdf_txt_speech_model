import calendar

print(calendar.weekheader(2))
print()
print(calendar.firstweekday())
print()
print(calendar.month(2020, 10))

print(calendar.monthcalendar(2020, 10))

print(calendar.calendar(2020))

day_of_the_week = calendar.weekday(2020, 10, 30)
print(day_of_the_week)

is_leap = calendar.isleap(2030)
print(is_leap)

how_many_leap_days = calendar.leapdays(2000,2021)
print(how_many_leap_days)
#exclusive_function_a_year_forward 