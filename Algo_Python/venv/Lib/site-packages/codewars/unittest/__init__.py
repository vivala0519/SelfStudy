
from codewars.unittest.testSurf import TestSurf
from codewars.unittest.testScraper import TestScraper
import unittest

class Test(object):
    def __init__(self, debug=False):
        """Initialize a unittest suite."""
        self.__loader = unittest.TestLoader()
        self.__suite = unittest.TestSuite()

        # add tests to the test suite
        self.__suite.addTests(self.__loader.loadTestsFromModule(TestSurf()))
        self.__suite.addTests(self.__loader.loadTestsFromModule(TestScraper()))

        # initialize a runner, pass it your suite and run it
        if debug: self.runner = unittest.TextTestRunner(verbosity=3)
        else: self.runner = unittest.TextTestRunner()
    
    def run(self):
        """Runs all tests added to the test suite.

        Returns
        -------
        Results
            Description of the test results
        """
        return self.runner.run(self.__suite)

    def addTest(self, test=None):
        """Add a unit test class with this function if needed
        preferably add the tests hard coded in the __init__ class.
        """
        if test is None: raise AttributeError("Argument should be a unittest class")
        self.__suite.addTest(self.__loader.loadTestsFromModule(test))