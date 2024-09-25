#!/usr/bin/env python3.11
number = int(input("input an interger number:"))

if number < 2:
      print("input a number greater than 1")
      number = int(input("input an interger number:"))


for item in range(2,number+1):
      valid = True
      i=2
      while i < item:
            if item%i == 0:
                  valid = False
                  break
            i+=1

      if valid:
            print(f"{item} is a prime")
      else:
            print(f"{item} is not a prime")