from fly_t import nextu
def max_alt(u0):
      if u0>1:
            return max(u0, max_alt(nextu(u0)))
      else:
            return 1