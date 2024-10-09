#!/usr/bin/env python3.11
import math
def shrink_min(s):
      min_s = min(s)
      for item in s:
            if item == min_s:
                  s.pop(s.index(item))
      
      return s

grades = [2, 18, 9, 5, 14, 2, 16, 19, 15, 13, 10]
print(shrink_min(grades))

def sortedm(nb, m):
      return sorted(nb,key = lambda n: n%m)
grades = [2, 18, 9, 5, 14, 2, 16, 19, 15, 13, 10]
print(sortedm(grades,6))

def mean_geo(nb):
      n = len(nb)
      log_g_mean = 0
      
      for item in nb:
            log_g_mean = math.log(item)
      return math.exp(log_g_mean/n)

print(mean_geo(grades))
