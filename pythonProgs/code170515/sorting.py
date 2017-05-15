def ins_sort_rec (seq, i):
  if i == 0: return
  
  ins_sort_rec(seq, i-1)
  j = i
  while j >0 and seq[j-1] > seq[j]:
    seq[j-1], seq[j] = seq[j], seq[j-1]
    j -=1
#---------------------------------------------
def ins_sort(seq):
  for i in range(1,len(seq)): # 0..i-1 sorted so far
    j = i # Start "walking" down
    while j > 0 and seq[j-1] > seq[j]: # Look for OK spot
      seq[j-1], seq[j] = seq[j], seq[j-1] # Keep moving seq[j] down
      j -= 1 # Decrement   j
#---------------------------------------------



def sel_sort_rec(seq, i):
  if i==0: return # Base case -- do nothing
  max_j = i # Idx. of largest value so far
  for j in range(i): # Look for a larger value
    if seq[j] > seq[max_j]: 
      max_j = j # Found one? Update max_j
  seq[i], seq[max_j] = seq[max_j], seq[i] # Switch largest into place
  sel_sort_rec(seq, i-1) # Sort 0..i-1



def sel_sort(seq):
  for i in range(len(seq)-1,0,-1): # n..i+1 sorted so far
    max_j = i # Idx. of largest value so far
    for j in range(i): # Look for a larger value
      if seq[j] > seq[max_j]: 
        max_j = j # Found one? Update max_j
    seq[i], seq[max_j] = seq[max_j], seq[i] # Switch largest into place


#----------------------------------------------
import math 
import random

N = 10
seq = [ random.randint(1, 100) for i in range(N)]
print seq
ins_sort_rec(seq, N-1) 
print seq


seq = [ random.randint(1, 100) for i in range(N)]
print seq
ins_sort(seq) 
print seq


seq = [ random.randint(1, 100) for i in range(N)]
print seq
sel_sort_rec(seq, N-1) 
print seq


seq = [ random.randint(1, 100) for i in range(N)]
print seq
sel_sort(seq) 
print seq










