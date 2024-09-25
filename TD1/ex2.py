#!/usr/bin/env python3.11
number = int(input("Enter a number (0 to stop) :"))
product = 1
while number !=0:
      product*=number
      number = int(input("Enter a number (0 to stop) :"))

print(f"Product:{product}")
