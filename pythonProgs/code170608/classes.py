#-----------instance objects --------------------------------------------------
class Complex:
  def __init__(self, real, imag):
    self.i = imag
    self.r = real
    
n = Complex(3,4)
#print n
#print n.i
#print n.r

#------------method objects--------------------------------------------------
class Dog:
 kind = 'canine' # class variable shared by all instances
 def __init__(self, name, years):
   self.name = name
   self.years = years
   self.tricks = []
   
 def humanYears(self):
  return 6
  
 def add_trick(self, trick):
   self.tricks.append(trick)
 
 def g(self):
  return 'hello world'

myDog = Dog('Chance', 7)

myDog.add_trick('roll over')


print myDog.name
print myDog.years
print myDog.tricks



y =  myDog.humanYears
print y





















