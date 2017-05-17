# ---------------------------------------------------
def max_perm(M):
  n = len(M) # How many elements?
  A = set(range(n)) # A = {0, 1, ... , n-1}
  count = [0]*n # C[i] == 0 for i in A


  for i in M: # All that are "pointed to"
    count[i] += 1 # Increment "point count"

  Q = [i for i in A if count[i] == 0] # Useless elements

  while Q: # While useless elts. left...
    i = Q.pop() # Get one
    A.remove(i) # Remove it
    j = M[i] # Who's it pointing to?
    count[j] -= 1 # Not anymore...

    if count[j] == 0: # Is j useless now?
      Q.append(j) # Then deal w/it next
  return A
   

#----------------------------------------------------
def naive_max_perm(M, A=None):
  if A is None: # The elt. set not supplied?
    A = set(range(len(M))) # A = {0, 1, ... , n-1}
  
  if len(A) == 1: return A # Base case -- single-elt. A
  B = set(M[i] for i in A) # The "pointed to" elements
  C = A - B # "Not pointed to" elements
  
  if C: # Any useless elements?
    A.remove(C.pop()) # Remove one of them
    return naive_max_perm(M, A) # Solve remaining problem
  
  return A # All useful -- return all
  

#----------------------------------------------------

def celeb(G):

  n = len(G)
  u, v = 0, 1            # The first two
  
  for c in range(2,n+1): # Others to check
    if G[u][v]: 
      u = c              # u knows v? Replace u
    else: 
      v = c              # Otherwise, replace v

  if u == n: 
    c = v              # u was replaced last; use v
  else: 
    c = u              # Otherwise, u is a candidate
  
  for v in range(n):     # For everyone else...
   if c == v: 
     continue           # Same person? Skip.
   if G[c][v]: 
     break              # Candidate knows other
   if not G[v][c]: 
     break              # Other doesn't know candidate
    
  else:
    return c           # No breaks? Celebrity!

  return None          # Couldn't find anyone

#------------------------------------------------------------

def naive_topsort(G, S=None):
  if S is None: 
  S = set(G)                 #   Default: All nodes

  if len(S) == 1: 
    return list(S)           #   Base case, single node

  v = S.pop()               # Reduction: Remove a node
  seq = naive_topsort(G, S) # Recursion (assumption), n-1
  min_i = 0

  for i, u in enumerate(seq):
    if v in G[u]: 
      min_i = i+1             # After all dependencies
    seq.insert(min_i, v)
    
  return seq
#-----------------------------------------------------------------------
def topsort(G):
  count = dict( (u,0)  for u in G )     # The in-degree for each node
  
  for u in G:
    for v in G[u]:
      count[v] += 1                     # Count every in-edge
  
  Q = [u for u in G if count[u] == 0]   # Valid initial nodes
  S = []                                # The result
    
  while Q:                              # While we have start nodes...
    u = Q.pop()                          # Pick one
    S.append(u)                          # Use it as first of the rest
    for v in G[u]:
      count[v] -= 1                      # "Uncount" its out-edges
      if count[v] == 0:                  # New valid start nodes?
        Q.append(v)                      # Deal with them next
  
  return S
#-----------------------------------------------------------------------




















































#--------------------------------------------------