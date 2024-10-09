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

def record(u):
      i =1
      rec =0
      while i<=u:
            max = max_alt(i)
            if max > rec:
                  print(f"{i}:{max}")
                  rec = max
            i +=1

record(17)


                        
