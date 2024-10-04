#!usr/bin/env python3.11
from matplotlib import pyplot as plt
from max_atl import max_alt
from fly_t import fly_t, nextu


def draw(n):
      if type(n) != int:
            raise TypeError("(draw) n must be an int!")
      flight = [n]
      while flight[-1] != 1:
            flight.append(nextu(flight[-1]))
      plt.title("Syracuse, N=" + str(n))
      plt.plot(flight)
      print("Close the graphic to continue...")
      plt.show()

def record(n):
      record_list = [max_alt(n)]
      for i in range(1,n):
            if max_alt(i) > max_alt(n):
                  return "it's not a recod"
                  break
            record_list.append(max_alt(i))
      return record_list

print(record(17))


                        
