day  = int(input("day ?"))
month  = int(input("month is ?"))
year  = int(input("year is ?"))

valid = True


      
if day >=1 and day<=31:
      if month >= 1 and month <=12:
            if month in (4,6,9,11) and day > 30:
                  valid = False
            elif month == 2 and year%4 == 0:
                  if day > 29:
                        valid = False
            elif month == 2 and year%4 != 0:
                  if day > 28:
                        valid = False
      else:
            valid = False
else:
      valid = False


if len(str(year)) != 4:
      valid= False

if valid:
      message = " this is  a valid date"
else:
      message = " this is  an invalid date"

print(message)