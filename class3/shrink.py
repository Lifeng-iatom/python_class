#!/usr/bin/env python3.11
import math
def shrink_min(s):
      s_min = sorted(s)
      s.pop(s.index(s_min[0]))
      return s

grades = [12, 18, 9, 5, 14, 2, 16, 19, 15, 13, 10]
print(shrink_min(grades))

def sortedm(nb, m):
      return sorted(nb,key = lambda n: n%m)

print(sortedm(grades,6))

def mean_geo(nb):
      n = len(nb)
      log_g_mean = 0
      
      for item in nb:
            log_g_mean = math.log(item)
      return math.exp(log_g_mean/n)

print(mean_geo(grades))
