class Employee: 
  empCount = 0                     #'Common base class for all employees'


  def __init__(self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1


  def displayCount(self):
    print "Total Employee %d" % Employee.empCount
    return Employee.empCount

  def displayEmployee(self):
    print "Name : ", self.name, ", Salary: ", self.salary

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

print '----------------------------------------------------'


    
mE = Employee("Me", 30)
a = mE.displayCount()
mE.displayEmployee()
print a
 
emp1 = Employee("Zara", 2000)   
emp1.displayEmployee()   

emp1.age = 7 # Add an 'age' attribute.
emp1.age = 8 # Modify 'age' attribute.
del emp1.age # Delete 'age' attribute.

print '----------------------------------------------------' 

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

print '----------------------------------------------------'    
    
    
    
    
    
    
    
    
    
    
    
    
    
    