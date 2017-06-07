'''
Note that in order to test something, we use one of the assert*() methods provided by the TestCase base class. If the test fails, an exception will be raised, and unittest will identify the test case as a failure. Any other exceptions will be treated as errors. This helps you identify where the problem is: failures are caused by incorrect results - a 5 where you expected a 6. Errors are caused by incorrect code - e.g., a TypeError caused by an incorrect function call.
'''

import unittest

class SimpleWidgetTestCase(unittest.TestCase): # Such a working environment for the testing code is called a fixture:
    def setUp(self):
        self.widget = Widget('The widget')
    
    def tearDown(self):
        self.widget.dispose()
        self.widget = None
        
class DefaultWidgetSizeTestCase(unittest.TestCase):
    def runTest(self):
        widget = Widget('The widget')
        self.assertEqual(widget.size(), (50, 50), 'incorrect default size')

class WidgetResizeTestCase(SimpleWidgetTestCase):
    def runTest(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')

'''
The way to run a test case will be described later. For now, note that to construct an instance of such a test case, we call its constructor without arguments:
'''

testCase = DefaultWidgetSizeTestCase()
print testCase