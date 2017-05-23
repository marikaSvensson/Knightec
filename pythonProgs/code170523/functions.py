# These are all the  functions/algorithms that are produced - these are called by main.py
# created by Marika Svensson 20170523

# Divide and conquer canonical algorithm (pp 118)
#input : set/sequence of elements


# --------------------   no 1: ---------------------------------------
def divide_and_conquer (S, divide, combine ):
  if (len(S) == 1 ): # the skyline is one element
    return S 
  L,R = divide(S)
  A = divide_and_conquer (L, divide, combine )
  B = divide_and_conquer (R, divide, combine )
  return combine(A,B)
#---------------------
def divide(S):
  L = S[: int(round(len(S)/2))]
  R = S[int(round(len(S)/2)):]
  return L,R
#---------------------  
def combine(A,B):
  S = [0]*( len(A) + len(B) )
  S[:len(A)] = A
  S[len(A):] = B
  return S
# ------------------------------------------------------------------
#------------------------- Searching by Halves ---------------------
def bisect_right(a, x, lo=0, hi=None):
  if hi is None:                 # Searching to the end
    hi = len(a)

  while lo < hi:                 # More than one possibility
    mid = (lo+hi)//2             # Bisect (find midpoint)
    
    if x < a[mid]: 
      hi = mid                   # Value < middle? Go left
    else: lo = mid+1             # Otherwise: go right

  return lo
# --------------------------------------------------------------------
#------------ Traversing search trees w. pruning ---------------------
#----------------------- class Node ----------------------------------
class Node:
 lft = None
 rgt = None 
 def __init__(self, key, val):
  self.key = key
  self.val = val
# ---------------------------------------------------------------------
# --------------global function----------------------------------------
def insert(node, key, val):
 
 if node is None: 
   return Node(key, val) # Empty leaf: add node here
 
 if node.key == key: 
   node.val = val # Found key: replace val
 elif key < node.key: # Less than the key?
   node.lft = insert(node.lft, key, val) # Go left
 else: # Otherwise...
   node.rgt = insert(node.rgt, key, val) # Go right
 
 return node

# --------------global function--------------------------------------
def search(node, key):

 if node is None: 
   raise KeyError # Empty leaf: it's not here
   
 if node.key == key: 
   return node.val # Found key: return val
 
 elif key < node.key: # Less than the key?
   return search(node.lft, key) # Go left
 else: # Otherwise...
   return search(node.rgt, key) # Go right
# ---------------------------------------------------------------------
#----------------------- class Tree ----------------------------------
class Tree: # Simple wrapper
 root = None
 
 def __setitem__(self, key, val):
  self.root = insert(self.root, key, val)
 
 def __getitem__(self, key):
   return search(self.root, key)
   
 def __contains__(self, key):
   try: 
     search(self.root, key)
   except KeyError: return False
   return True
#-------------------------------------------------------------------------
#------------SORTED ARRAYS TREES, DICTS: CHOICES--------------------------
#------------------------------------------------------------------------- 

# Fastest : hash table --> python dict structure <T(n)> = O(1) 
# requirement: ba able to compute hash value for objects

#------------------- Selection w. bisection  --------------------

# P) find  k:th largest nbr in unsorted seq 'seq' w. T(n) = O(n)
# Si) heap --> T(n) = O( n lgk ) = O( n ) if k << n 
# Sii) T(n) = T(n/2) + n


def partition( seq ): 
  pi, seq = seq[0], seq[1:]
  lo = [x for x in seq if x <= pi]
  hi = [x for x in seq if x >  pi]
  
  return lo, pi, hi

def select(seq, k):
  lo, pi, hi = partition( seq )
  
  m = len(lo)
  
  if m == k:
    return pi
  elif m < k:
    return  select(seq , k -m-1)
  else:
    return  select(lo , k)

#-------------------------------------------------------------------------
#------------SORTING IN GARANTEED LINEAR TIME -------------------------
#-------------------------------------------------------------------------  
  
# 1) divide seq in C(small constant) groups
# 2) find median in each (w. simple sorting algorithm)
# 3) find median among these medians (w linear selection algorithm recursively)

  
#-------------------------------------------------------------------------
#------------SORTING BY HALVES - QUICKSORT -------------------------------
#-------------------------------------------------------------------------
def quicksort (seq):
  if len(seq) <= 1:                   # base case 
    return seq   
  
  lo, pi, hi = partition(seq)        # pi is in its place
  
  return quicksort(lo) + [pi] + quicksort(hi)

#-------------------------------------------------------------------------
#------------SORTING BY HALVES - MERGE SORT ------------------------------
#----------------------heapq.merge better in python-----------------------
def mergesort(seq):  
  mid = len(seq)//2                # midpoint for division
  
  l, r = seq [:mid], seq [mid:]
  
  if len(l) > 1:                   # sort by halves
    l = mergesort(l)
  if len(r) > 1:
   r = mergesort (r)
  
  res = []
  
  while l and r:                    # Neither half is empty
   if l[-1] >= r[-1]:                # lft has greatest last value
     res.append (l.pop() )            # Append it
   else:                             # rgt has greatest last value
     res.append (r.pop()  )          # Append it
  res.reverse()
  return(l or r) + res        # Also add the remainder


  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  