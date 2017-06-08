#try:
# raise KeyboardInterrupt
#finally:
# print('Goodbye, world!')
 
 
 
def divide(x, y):
 try:
   result = x / y
 except ZeroDivisionError:
   print("division by zero!")
 else:
   print("result is", result)
 finally:
   print("executing finally clause")
   

x = 1
y = 2
divide(x, y)

x = 1
y = 0
divide(x, y)


#_---------------------------------------------------
'''
The with
statement allows objects like files to be used in a way that ensures they are always cleaned up promptly and correctly.
'''

with open("myfile.txt") as f:
  for line in f:
    print line,

'''
After the statement is executed, the file f is always closed, even if a problem was encountered while processing the
lines. Objects which, like files, provide predefined clean-up actions will indicate this in their documentation.
'''


















