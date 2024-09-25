#!/usr/bin/env python3.11
number = int(input("input an interger number:"))

if number < 2:
      print("input a number greater than 1")
      number = int(input("input an interger number:"))

counter = 0
item = number + 1

while counter <25:
      valid = True
      i=2
      while i < item:
            if item%i == 0:
                  valid = False
                  break
            i+=1

      if valid:
            print(item)
            counter +=1
      item +=1