import unittest

from root_finders import Bisection

class testRootFinders(unittest.TestCase):
    """

    """

    def test_bisection_linear_function(self):
        function_array = [(1,1),-1]
        initial_guess = [-5,5]
        root = 1

        bisection = Bisection(function_array, initial_guess)
        bisection._find_root()

        self.assertEqual(root, bisection.root)
    
    def test_bisection_quadratic_function(self):
        function_array = [(1,2),-4]
        initial_guess = [-5,0]
        root = -2

        bisection = Bisection(function_array, initial_guess)
        bisection._find_root()

        self.assertEqual(root, bisection.root)
        
        function_array = [(1,2),-4]
        initial_guess = [0,5]
        root = 2

        bisection = Bisection(function_array, initial_guess)
        bisection._find_root()

        self.assertEqual(root, bisection.root)
