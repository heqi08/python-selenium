import unittest
import HTMLReport
from testSuites.Test_Amazon import TestAmazon
import os
import getcwd

path = getcwd.get_cwd()
file_path = os.path.join(path, 'report\\')

if __name__ == "__main__":
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    suite.addTests(loader.loadTestsFromTestCase(TestAmazon))
    runner = HTMLReport.TestRunner(
        title='TW homework automation test report',
        lang='en'
    )
    runner.run(suite)
