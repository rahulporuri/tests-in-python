class Bisection():
    """

    """

    def __init__(self, function, initial_guess):
        self.function = function
        self.a, self.b = initial_guess

    def _find_root(self):
        func_value = self.function(self.a)*self.function(self.b)
        if abs(func_value) + func_value != 0:
            self.a = raw_input()
            self.b = raw_input()
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
    """

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
            estimate_root = (self.a*self.function(self.b) - self.b*self.function(self.a))/(self.function(self.b) - self.function(self.a))
            while self.function(estimate_root) != 0:
                func_value = self.function(self.a)*self.function(estimate_root)
                if abs(func_value) + func_value != 0:
                    self.a = estimate_root
                    estimate_root = (self.a*self.function(self.b) - self.b*self.function(self.a))/(self.function(self.b) - self.function(self.a))
                else:
                    self.b = estimate_root
                    estimate_root = (self.a*self.function(self.b) - self.b*self.function(self.a))/(self.function(self.b) - self.function(self.a))

        self.root = estimate_root


class NewtonRhapson():
    """

    """

    def __init__(self, function, Dfunction, initial_guess):
        self.function = function
        self.Dfunction = Dfunction
        self.a = initial_guess

    def _find_root(self):
        estimate_root = self.a
        func_value = self.function(estimate_root)
        while func_value != 0:
            estimate_root = estimate_root - self.function(estimate_root)/self.Dfunction(estimate_root)
            func_value = self.function(estimate_root)

        self.root = estimate_root


if __name__ == "__main__":
    print "bisection"
    function = lambda x: x**3+x**2+x-2
    bisection = Bisection(function, [-1, 1])
    bisection._find_root()
    print bisection.root

    print "secant"
    function = lambda x: x**2-4
    secant = Secant(function, [-5, 0])
    secant._find_root()
    print secant.root

    print "newton-rhapson"
    function = lambda x: x**2-4
    dfunction = lambda x: 2*x
    newton_rhapson = NewtonRhapson(function, dfunction, -4)
    newton_rhapson._find_root()
    print newton_rhapson.root
