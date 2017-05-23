#------------------------------------------------------------------------- 
# Created by Marika Svensson 20170523
# Ch 6 - Python Programming
from functions import * # import all the functions
import time

#------------------------------------------------------------------------- 


#------------------------------------------------------------------------- 
print "----------------------Tree-Shaped Problems:------------------"
#------------------------------------------------------------------------- 
# Asymptotic T(n) = 2T(n/2) + n = O(nlgn): Canonical Divide and conquer

# skyline problem
#(L,H.R) = (Left X-coord, height, right X-coord ) of  a building
#        represent rectangular silouette

A = [1]*10**5
B = [3]*10**5

S = combine(A,B)
L,R = divide(S)

t0 = time.time()
divide_and_conquer (S, divide, combine )
t1 = time.time()

print  t1-t0

print 3//2, 4//2, 11//3
#------------------------------------------------------------------------- 
#------------------------- Searching by Halves ---------------------------
#------------------------------------------------------------------------- 
a = [0, 2, 3, 5, 6, 8, 8, 9]
print bisect_right(a, 5) # returns value after 5

seq = "I aim to misbehave".split()
print seq
dec = sorted((len(x), x) for x in seq)
print dec

keys = [k for (k, v) in dec]
vals = [v for (k, v) in dec]
print vals[bisect_right(keys, 3)]
#------------------------------------------------------------------------- 
#---------------------- searching trees w D&C ----------------------------
#------------------------------------------------------------------------- 
tree = Tree()
tree["a"] = 42
print tree["a"]
print "b" in tree
#-------------------------------------------------------------------------
#------------SORTED ARRAYS TREES, DICTS: CHOICES--------------------------
#------------------------------------------------------------------------- 
# P) find  k:th largest nbr in unsorted seq 'seq' w. T(n) = O(n)
import random

M = 10
k = 6
seq = [x for x in range(M)]

seq2 =  select(seq, k)

print seq2, k, seq  
#------------------------------------------------------------------------- 
#------------------------------------------------------------------------- 
#------------------------------------------------------------------------- 

















































    