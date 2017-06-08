print '-----------------------------------------------------------'
import sys

try:
  f = open('myfile.txt')
  s = f.readline()
  i = int(s.strip())

except OSError as err:
  print("OS error: {0}".format(err))
  
except ValueError:
  print("Could not convert data to an integer.")

except:
  print("Unexpected error:", sys.exc_info()[0])
  raise

print '-----------------------------------------------------------'
for arg in sys.argv[1:]:
 try:
    f = open(arg, 'r')
 except OSError:
   print('cannot open', arg)
 else:
  print(arg, 'has', len(f.readlines()), 'lines')
  f.close()

print '-----------------------------------------------------------'
try:
 raise Exception('spam', 'eggs')
except Exception as inst:
 print(type(inst))               # the exception instance
 print(inst.args)                # arguments stored in .args
 print(inst)                     # __str__ allows args to be printed directly,
                                 # but may be overridden in exception subclasses
 x, y = inst.args                # unpack args
 print('x =', x)
 print('y =', y)
 
 
print '-----------------------------------------------------------'
def this_fails():
  x = 1/0
  
  
try:
  this_fails()
except ZeroDivisionError as err:
  print 'Handling run-time error:\n', err
print '-----------------------------------------------------------'