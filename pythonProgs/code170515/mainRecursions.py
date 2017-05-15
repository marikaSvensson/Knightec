# ------------------ import libraries ---------------------------
#import matplotlib
#import numpy as np
#import matplotlib.cm as cm
#import matplotlib.mlab as mlab
#import matplotlib.pyplot as plt
import math

# ------------------ function definitions ------------------------
def S(seq, i=0):
  if i == len(seq): 
    return 0
  else:
    return S(seq, i+1) + seq[i]

def T(seq, i=0):
  if i == len(seq): 
    return 1
  return T(seq, i+1) + 1

# ------------------ sorting algorithms:------------------  
# gnome sort:
def gnomesort(seq):
  i = 0
  while i < len(seq):
    if i == 0 or seq[i-1] <= seq[i]:
      i += 1
    else:
      seq[i], seq[i-1] = seq[i-1], seq[i]
      i -= 1 

# merge sort(ing) algorithm:
def mergesort(seq):
  mid = len(seq)//2
  lft, rgt = seq[:mid], seq[mid:]
  if len(lft) > 1: 
    lft = mergesort(lft)
  if len(rgt) > 1: 
    rgt = mergesort(rgt)

  res = []
  while lft and rgt:
    if lft[-1] >=rgt[-1]:
      res.append(lft.pop())
    else:
      res.append(rgt.pop())

  res.reverse()
  return (lft or rgt) + res
#---------------------- main program -------------------------------    
    
a = range(1, 10)
#print a, sum(a)
print "S(a)", S(a)
print "T(a)", T(a)
