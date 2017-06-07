'''
existing test code  to run from unittest, without converting every old test function toa TestCase subclass.

For this reason, unittest provides a FunctionTestCase class. This subclass of TestCase can be used to wrap an existing test function. Set-up and tear-down functions can also be provided.

Given the following test function:

def testSomething():
    something = makeSomething()
    assert something.name is not None
    # ...
one can create an equivalent test case instance as follows:

testcase = unittest.FunctionTestCase(testSomething)

If there are additional set-up and tear-down methods that should be called as part of the test case’s operation, they can also be provided like so:

testcase = unittest.FunctionTestCase(testSomething,
                                     setUp=makeSomethingDB,
                                     tearDown=deleteSomethingDB)
'''