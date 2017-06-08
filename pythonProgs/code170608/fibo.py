# ------------- Fibonacci numbers ------------------------
#---------------------------------------------------------
def fib(n): # write Fibonacci series up to n
  a, b = 0, 1
  print ''
  while b < n:
    print  b,
    a, b = b, a+b
  print '' 
#---------------------------------------------------------  
def fib2(n): # return Fibonacci series up to n
  result = []
  a, b = 0, 1
  
  while b < n:
    result.append(b)
    a, b = b, a+b
  print ''
  return result

#---------------------------------------------------------
'''
the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". That
means that by adding this code at the end of your module:
'''

if __name__ == "__main__":
  import sys
  
  fib(int(sys.argv[1]))








