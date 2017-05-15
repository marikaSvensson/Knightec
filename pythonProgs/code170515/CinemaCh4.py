# task: how to permute the best when M people want to 
# change seats

# ---------------- import --------------------------





#------------------ functions ----------------------
def naive_max_perm(M, A=None):
  if A is None: # The elt. set not supplied?
    A = set(range(len(M))) # A = {0, 1, ... , n-1}
    print "A1= ", A
  if len(A) == 1: 
    print "A2= ", A
    return A # Base case -- single-elt. A
  
  B = set(M[i] for i in A) # The "pointed to" elements
  C = A - B # "Not pointed to" elements
  if C: # Any useless elements?
    A.remove(C.pop()) # Remove one of them
    print "A3= ", A
    return naive_max_perm(M, A) # Solve remaining problem
  return A # All useful -- return all
  
# ------------------- main progs----------------------


# varable defs:
M = [2, 2, 0, 5, 3, 5, 7, 4] # mapping array 


# function call:
print "naive_max_perm(M) = ", naive_max_perm(M)
print "M= ", M


# -------------- end --------------------------------

