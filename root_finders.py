class RootFinder():
    """ this class defines the model upon which the rest of the
    root finders are based upon.
    
    The init method takes one or two function objects as input
    and an initial guess, which might be two values or one,
    depending on the solver. a and b are the corresponding initial
    guess that the user provides.

    NOTE : all of the classes only support root finding for polynomial
    functions, which take only one input.

    NOTE : if the sign of the function value isnt different for the
    two initial guesses provided, the user will be prompted to provide
    other initial values.

    the _find_root private method implements the specific algorithm
    being used to estimate the root.

    """

    def __init__(self):
        pass
    def _find_root(self):
        pass

class Bisection():
    """ this class implements the bisection method to estimate
    the root of the polynomial function given as input.

    starting with the average of the two initial guesses, we either
    move from the average value to the left or towards the right
    depending on the sign of the product of the function values

    """

    def __init__(self, function, initial_guess):
        self.function = function
        self.a, self.b = initial_guess

    def _find_root(self):
        func_value = self.function(self.a)*self.function(self.b)
        if abs(func_value) + func_value != 0:
            self.a = raw_input('a=')
            self.b = raw_input('b=')
        else:
            estimate_root = (self.a + self.b)/2.
            while self.function(estimate_root) != 0:
                func_value = self.function(self.a)*self.function(estimate_root)
                if abs(func_value) + func_value != 0:
                    self.a = estimate_root
                    estimate_root = (self.a + self.b)/2.
                else:
                    self.b = estimate_root
                    estimate_root = (self.a + self.b)/2.

        self.root = estimate_root


class Secant():
    """ this class implements the secant method to estimate the
    root of the polynomial function given as input.

    """

    def __init__(self, function, initial_guess):
        self.function = function
        self.a, self.b = initial_guess

    def _find_root(self):
        func_value = self.function(self.a)*self.function(self.b)
        if abs(func_value) + func_value != 0:
            self.a = raw_input('a=')
            self.b = raw_input('b=')
        else:
            estimate_root = ((self.a*self.function(self.b) - self.b*self.function(self.a))/
                            (self.function(self.b) - self.function(self.a))
            )
            while self.function(estimate_root) != 0:
                func_value = self.function(self.a)*self.function(estimate_root)
                if abs(func_value) + func_value != 0:
                    self.a = estimate_root
                    estimate_root = ((self.a*self.function(self.b) - self.b*self.function(self.a))/
                                    (self.function(self.b) - self.function(self.a))
                )
                else:
                    self.b = estimate_root
                    estimate_root = ((self.a*self.function(self.b) - self.b*self.function(self.a))/
                                    (self.function(self.b) - self.function(self.a))
                )

        self.root = estimate_root


class NewtonRhapson():
    """ this class implements the newton rhapson method to estimate
    the root of the polynomial function given as input.

    NOTE : this method differs from the above in the fact that it
    needs the derivative of the polynomial, called Dfunction here,
    along with the polynomial, called function.

    NOTE : it also only needs one initial guess.

    """

    def __init__(self, function, Dfunction, initial_guess):
        self.function = function
        self.Dfunction = Dfunction
        self.a = initial_guess

    def _find_root(self):
        estimate_root = self.a
        func_value = self.function(estimate_root)
        while func_value != 0:
            estimate_root = estimate_root - (self.function(estimate_root)/
                                            self.Dfunction(estimate_root)
            )
            func_value = self.function(estimate_root)

        self.root = estimate_root


if __name__ == "__main__":
    print "bisection method"
    function = lambda x: x**3+x**2+x-2
    bisection = Bisection(function, [-1, 1])
    bisection._find_root()
    print bisection.root

    print "secant method"
    function = lambda x: x**2-4
    secant = Secant(function, [-5, 0])
    secant._find_root()
    print secant.root

    print "newton-rhapson method"
    function = lambda x: x**2-4
    dfunction = lambda x: 2*x
    newton_rhapson = NewtonRhapson(function, dfunction, -4)
    newton_rhapson._find_root()
    print newton_rhapson.root
