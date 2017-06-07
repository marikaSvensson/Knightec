'''
unittest supports:
 
  - test automation
  - sharing of setup and shutdown code for tests
  - aggregation of tests into collections
  - independence of the tests from the reporting framework.
Via:  
  - test fixture (using TestCase, the setUp() and tearDown() methods can be overridden to provide initialization and cleanup for the fixture, With FunctionTestCase, existing functions can be passed to the constructor for these purposes. )
  - test case ( TestCase and FunctionTestCase classes)
  - test suite (implemented by the TestSuite class)
  - test runner (is an object that provides a single method, run(), which accepts a TestCase or TestSuite object as a parameter, and returns a result object. The class TestResult is provided for use as the result object.  unittest provides the TextTestRunner as an example test runner which reports test results on the standard error stream by default)
  
'''
# ----- Here is a short script to test three string methods:----------
import unittest
# tests in alphabetical order
class TestStringMethods(unittest.TestCase):

    def test_upper(self): # test case 1
        print self
        print 'foo'.upper()
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self): # test case 2
        print self
        
        print 'FOO'.isupper()
        print 'Foo'.isupper()
        
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self): # test case 3
        s = 'hello world'
        print self
        print s.split()
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main() #provides a command-line interface to the test script.
''' Alt: 
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
    
    commandline alt: python -m unittest unitTests
    or:
    python -m unittest <pyFileName/aka Module>.<testClass>.<testMethod>
    .
    to discover:
    python -m unittest discover -s project_directory -p "*.py"
    python -m unittest discover project_directory "*.py"
    
    As well as being a path it is possible to pass a package name, for example myproject.subpackage.test, as the start directory. The package name you supply will then be imported and its location on the filesystem will be used as the start directory.
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    