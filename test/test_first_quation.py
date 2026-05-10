# test_first_equation.py

import unittest
import first_equation

# class TestFirst(unittest.TestCase):

#     def test_find_x(self):
#         args = (10, 10)
#         self.assertEqual(first_equation.find_x(*args), -1)
#         args = (0, 0)
#         self.assertEqual(first_equation.find_x(*args), "ALL")
#         args = (0, 10)
#         self.assertEqual(first_equation.find_x(*args), "NONE")

# if __name__ == '__main__':
#     unittest.main(verbosity=2)

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('python'.upper(), 'PYTHON')

    def test_isupper(self):
        self.assertTrue('PYTHON'.isupper())
        self.assertFalse('Python'.isupper())

    def test_islower(self):
        self.assertTrue('python'.islower())
        self.assertFalse('PYTHON'.islower())

    def test_split(self):
        test_string = 'python is a best language'
        self.assertEqual(test_string.split(),
                        ['python', 'is', 'a', 'best', 'language'])
        # check that test_string.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            test_string.split(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)