#!/usr/bin/env python3.11
def loop(i):
      if i==0:
            print("go!")
      else:
            print(i)
            loop(i-1)

loop(3)

def seqence(firstvalue,a,b,n):
      if n == 0:
            return firstvalue
      else:
            firstvalue =seqence(firstvalue,a,b,n-1)
            return a*firstvalue+b

print(seqence(1,2,1,3))

def fac(n):
      if n <= 1:
            return 1
      else:
            return n * fac(n-1)

print(fac(5))

def gcd(a,b):
      if b == 0:
            return a
      else:
            return gcd(b,a%b)

print(gcd(5,10))
print(gcd(11,10))
print(gcd(11,0))