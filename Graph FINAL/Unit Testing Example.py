'''
Example of unit testing in python
'''

def add(x, y):
    return x + y

import unittest
class UnitTesting(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add(2, 3), 5)

    def test_2(self):
        self.assertEqual(add(5, 6), 11)

if __name__ == "__main__":
    unittest.main()

'''If we do unit testing on another module then use the following code'''

import unittest

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(2, 4), 6)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_add2(self):
        self.assertEqual(calc.add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()