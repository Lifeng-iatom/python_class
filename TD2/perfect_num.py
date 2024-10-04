import math
def perfect_num(n):
      n_root = math.sqrt(n)
      total = 1
      for i in range(2,n):
            if i < n_root and n%i == 0:
                  total = total + i + n/i

      if total == n:
            return True
      else:
            return False

def all_perfect(a,b):
      for n in range(a,b+1):
            if perfect_num(n):
                  print(n)

def is_prime(item):
      valid = True
      i=2
      while i < item:
            if item%i == 0:
                  valid = False
                  break
            i+=1

      if valid:
            return True
      else:
            return False
            
def perfect_num_n(n):
      for i in range(1,n+1):
            a = pow(2,i+1)-1
            if is_prime(a):
                  print(pow(2,i) * a) 



print(perfect_num(28))
print(perfect_num(27))
all_perfect(2,10000)
perfect_num_n(29)