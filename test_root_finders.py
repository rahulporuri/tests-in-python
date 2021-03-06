import unittest

from root_finders import Bisection, Secant, NewtonRhapson


class testRootFinders(unittest.TestCase):
    """ tests the root finding methods implemented in root_finders.py
    to verify the results they produce. the methods defined herein
    follow a similar layout -

    1. define the function, initial guess and known root of the polynomial
    2. instantiate the class being tested with the relevant inputs
    3. check that the root value computed is the same as that expected.

    """

    def test_bisection_linear_function(self):
        function = lambda x: x-1
        initial_guess = [-5, 5]
        root = 1

        bisection = Bisection(function, initial_guess)
        bisection._find_root()

        self.assertEqual(root, bisection.root)

    def test_bisection_quadratic_function_1(self):
        function = lambda x: x**2-4
        initial_guess = [-5, 0]
        root = -2

        bisection = Bisection(function, initial_guess)
        bisection._find_root()

        self.assertEqual(root, bisection.root)

    def test_bisection_quadratic_function_2(self):
        function = lambda x: x**2-4
        initial_guess = [0, 5]
        root = 2

        bisection = Bisection(function, initial_guess)
        bisection._find_root()

        self.assertEqual(root, bisection.root)

    def test_secant_linear_function(self):
        function = lambda x: x-1
        initial_guess = [-5, 5]
        root = 1

        secant = Secant(function, initial_guess)
        secant._find_root()

        self.assertEqual(root, secant.root)

    def test_secant_quadratic_function_1(self):
        function = lambda x: x**2-4
        initial_guess = [-5, 0]
        root = -2

        secant = Secant(function, initial_guess)
        secant._find_root()

        self.assertEqual(root, secant.root)

    def test_newton_rhapson_quadratic_function_1(self):
        function = lambda x: x**2-4
        Dfunction = lambda x: 2*x
        initial_guess = -4
        root = -2

        newton_rhapson = NewtonRhapson(function, Dfunction, initial_guess)
        newton_rhapson._find_root()

        self.assertEqual(root, newton_rhapson.root)
