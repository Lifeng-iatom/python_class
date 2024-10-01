'''
def root_fun(a,b,c):
      if b**2-4*a*c>0:
            print("have 2 roots")
      elif b**2-4*a*c == 0:
            print("have 1 roots")
      else b**2-4*a*c<0:
            print("have 0 roots")
            '''

def norm(x,y):
      x2 = x ** 2
      y2 = y ** 2
      return (x2 + y2) ** 0.5


print(norm(1,1))

print(norm(4,3))