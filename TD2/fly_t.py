def nextu(un):
      if un % 2 == 0:
            return un/2
      else:
            return 3*un + 1
def fly_t(u0):
      
      if u0>1:
            return 1 + fly_t(nextu(u0))
      else:
            return 0

