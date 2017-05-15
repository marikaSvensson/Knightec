#---------------------- import libs --------------------
from random import randrange
import time


#---------------------- alg 1 --------------------
t0 = time.time()
seq = [randrange(10**10) for i in range(1000)]
dd = float("inf")
for x in seq:
  for y in seq:
    if x == y: 
      continue
    else:
      d = abs(x-y)
    if d < dd:
      xx, yy, dd = x, y, d
t1 = time.time()

total = t1-t0
print total
print xx, yy

#---------------------- alg 2 --------------------
t0 = time.time()
seq.sort()
dd = float("inf")
for i in range(len(seq)-1):
  x, y = seq[i], seq[i+1]
  if x == y:  
    continue
  d = abs(x-y)
  if d < dd:
    xx, yy, dd = x, y, d
    
t1 = time.time()

total2 = t1-t0
print total2

# -------------------- end ----------------------------