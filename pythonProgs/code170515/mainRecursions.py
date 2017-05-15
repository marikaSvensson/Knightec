
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math

def S(seq, i=0):
  if i == len(seq): 
    print i, "in if"
    return 0
  else:
    print i, "in elses"
    return S(seq, i+1) + seq[i]
    
    
a = range(10)
#print a, sum(a)
#print S(a)
S(a)
