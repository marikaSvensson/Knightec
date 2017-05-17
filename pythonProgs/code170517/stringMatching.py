# does not work yet ..

t  = "kfdjgfsngklsnklnklss"
s = "ss"


print len(t)
#any( s == t[i:i+len(s)])
for i in range( len(t) - len(s) + 1):
  print i , ": ", s == t[i:i+len(s)], " : ",  t[i:i+len(s)]
  
  
  
#-------------1990----------- Karp- Rabin algorithm -------------------------
# pseudo code:
rs = []
for c in s:
  rs.append(c)

for c in t[:len(s)];
  rt.append(c)
 
if rs() == rt(): ...

for i in range(len(s), len(t)):
  rt.skip(t[i-len(s)])
  rt.append(t[i]) 
   
  if rs() = rt():
    # check i s s == t[i-lens +1 : i +i]
    #if equal --> found match  O(s) = T(n)
    # else : P = (1/|s|) --> O(1) = T(n)
    
    # tot time : O(s + t #match*s) = T(n)
 
   
# ADT construction:

# division method 

# treat x as multidigit array in base a(lphabet size)
#i.e. u -> u*a + O(c)
























