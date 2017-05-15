# prime

def is_prime(n):
  for i in range(2,n):
    if n % i == 0: 
      return False
    else:
      return True 
      

n = 21
a = []
for i in range(2,n):
  if (is_prime(i)):
     a.append(i)
print a 
  