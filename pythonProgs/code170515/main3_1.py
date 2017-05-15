

# --------------------- functions ---------------------------------
def f (x):
  return x**x
#---------------- end function definitions ------------------------

m = 3
n = 10

print sum(f(i) for i in range(m, n+1))


s = 0
for i in range(m, n+1):
  s += f(i)

print s, range(m, n+1)




  