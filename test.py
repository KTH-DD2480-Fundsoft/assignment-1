#!/usr/bin/python3
''' 
Runs all unit and system tests in 'test_decide.py' with file prefix "test_".
'''
import unittest

loader = unittest.TestLoader()
tests = loader.discover('test_decide')

test_runner = unittest.TextTestRunner()
test_runner.run(tests)


