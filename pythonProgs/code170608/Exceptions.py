'''
Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it.
Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs.:
'''
'''
It is possible to write programs that handle selected exceptions. Look at the following example, which asks the user
for input until a valid integer has been entered, but allows the user to interrupt the program (using Control-C
or whatever the operating system supports); note that a user-generated interruption is signalled by raising the
KeyboardInterrupt exception.
'''
while True:
  try:
    x = int(input("Please enter a number: "))
    break
  except ValueError:
    print("Oops! That was no valid number. Try again...")
    
#---------------------------------------------------------
class B(Exception):
  pass
  
class C(B):
  pass
  
class D(C):
  pass
  

for cls in [B, C, D]:
  try:
    raise cls()
  except D:
    print("D")
  except C:
    print("C")
  except B:
    print("B")