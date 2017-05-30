 
filename = 'fileIOdata.txt'
fileobject = open(filename, 'r+')

print fileobject.read()

fileobject.write('i wrote this line ')