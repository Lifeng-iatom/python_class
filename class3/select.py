#!/usr/bin/env python3.11
MONTHS = ("jan", "feb", "mar", "apr", "may", "jun",
      "jul", "aug", "sep", "oct", "nov", "dec")
def select(char):
      
      return [m for m in MONTHS if char in m]

print(select('j'))