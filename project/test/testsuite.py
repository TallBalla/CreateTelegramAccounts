import unittest
import FileHandlerCase


suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(FileHandlerCase))


runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)
