def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                Leap_year = "yes"
            else:
                Leap_year = "no"
        else:
            Leap_year = "yes"
    else:
        Leap_year = "no"
    return Leap_year

def days_in_month(yr,mn):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if mn == 2:
        is_leap_year = is_leap(yr)
        if is_leap_year == "yes":
            days = 29
        else:
            days = 28
        return days
    else:
        days = month_days[mn+1]
        return days

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)