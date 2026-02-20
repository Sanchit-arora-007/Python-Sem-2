date = int(input('Enter date: '))
month = int(input('Enter month: '))
year = int(input('Enter year: '))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in_months= [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date += 1

    if date > days_in_months[month - 1]:
        date = 1
        month += 1

        if month > 12:
            month = 1
            year += 1
else:
    days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    date += 1

    if date > days_in_months[month - 1]:
        date = 1
        month += 1

        if month > 12:
            month = 1
            year += 1
print('Next day is:', date,'/', month, '/', year)