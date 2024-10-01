#!/usr/bin/env python3.11
import math

#norm function
def norm(x,y):
      x2 = x ** 2
      y2 = y ** 2
      return (x2 + y2) ** 0.5


print(norm(1,1))

print(norm(4,3))

#weight function
def weight(dia,hei):
      return math.pi*(dia/2)**2*hei

weight1=weight(17,3)
weight2 = weight(19,3)
weight3 = weight(17,4)

print(f"{weight1:.2f},{weight2:.2f},{weight3:.2f}",sep= " ")


def root(a,b,c):
      if not a==0:
            delta = b ** 2 - 4 * a * c
            if delta < 0:
                  return "there is no sulution"
            elif delta > 0:
                  return (((-b - delta ** 0.5) / (2 * a),((-b + delta ** 0.5) / (2 * a))))
            else:
                  return (-b / (2 * a))
      else:
            return -c/b

a = root(1,3,-4)
b = root(1,-2,1)
c = root(0,1,1)
print(a,b,c)
