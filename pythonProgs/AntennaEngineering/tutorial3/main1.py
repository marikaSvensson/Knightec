import math

PI = math.pi
print math.cos(110*PI/180.0)
print math.cos(60*PI/180.0), math.sqrt(3)/2
Pe = 2*PI/(31.27 + 1) + PI*0.0398**2*(math.cos(60*PI/180.0)-math.cos(110*PI/180.0))
Ph = 2*PI/(40.2 + 1) 
print  Pe, Ph , (Ph + Pe), 10*math.log(2*PI/(Ph + Pe), 10)

print 20 *math.log(0.0565/2, 10)
