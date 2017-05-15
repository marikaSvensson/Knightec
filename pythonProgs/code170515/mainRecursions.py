import math

def S(seq, i=0):
  if i == len(seq): 
    return 0
  else:
    return S(seq, i+1) + seq[i]
    
    
a = np.zeros(1,10)

print S(a)