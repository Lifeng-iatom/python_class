MONTHS = ("jan", "feb", "mar", "apr", "may", "jun",
      "jul", "aug", "sep", "oct", "nov", "dec")
print(MONTHS[1])

def month_name(tulpe_date):
      index_m = tulpe_date[1]
      return MONTHS[index_m-1]


print(month_name((1990,12,12)))

def period(m1,m2):
      if m1< 1 or m1>12:
            print("Error")
      if m2< 1 or m2>12:
            print("Error")

      if m1 < m2:
            return MONTHS[m1:m2-1]
      else:
            return None
print(period(1,5))




