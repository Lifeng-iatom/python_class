#!/usr/bin/env python3.11
def table():
      for item in range(2,10):
            for j in range(item,10):
                  print (f"{item}*{j}",end="  ")
            print()

table()
