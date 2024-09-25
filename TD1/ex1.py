def is_leap_year(year):
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def validate_date(day, month, year):
    
    valid = True
    
  
    if month < 1 or month > 12:
        print("Invalid month! Month must be between 1 and 12.")
        valid = False
    
   
    if day < 1 or day > 31:
        print("Invalid day! Day must be between 1 and 31.")
        valid = False

    
    if valid:

        if month in [4, 6, 9, 11] and day > 30:
            print(f"Invalid day! Month {month} cannot have more than 30 days.")
            valid = False
        
        if month == 2:
            if is_leap_year(year):
                if day > 29:
                    print(f"Invalid day! February in a leap year can only have up to 29 days.")
                    valid = False
            else:
                if day > 28:
                    print(f"Invalid day! February in a non-leap year can only have up to 28 days.")
                    valid = False
    
  
    if valid:
        print(f"{day:02d} {month:02d} {year} is a valid date.")
    else:
        print(f"{day:02d} {month:02d} {year} is an invalid date.")

# Test cases
validate_date(30, 2, 2015)  # Expected: Invalid date (February can't have 30 days)
validate_date(31, 1, 2017)  # Expected: Valid date
validate_date(31, 4, 2021)  # Expected: Invalid date (April can't have 31 days)
validate_date(29, 2, 2020)  # Expected: Valid date (Leap year)
validate_date(29, 2, 2019)  # Expected: Invalid date (Not a leap year)
