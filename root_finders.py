class Bisection():
    """

    """

    def __init__(self, function_array, initial_guess):
        self.function_array = function_array
        self.a, self.b = initial_guess

    def _find_root(self):
        function = lambda x : sum([coeff*(x**power) for coeff, power in self.function_array[:-1]])+self.function_array[-1]
        func_value = function(self.a)*function(self.b)
        if abs(func_value) + func_value != 0:
            self.a = raw_input()
            self.b = raw_input()
        else:
            estimate_root = (self.a + self.b)/2.
            while function(estimate_root) != 0:
                func_value = function(self.a)*function(estimate_root)
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



if __name__ == "__main__":
    print "bisection"
    bisection = Bisection([(1,3), (1,2), (1,1),-2], [-1,1])
    bisection._find_root()
    print bisection.root

    print "secant"
    function = lambda x : x**2-4
    secant = Secant(function, [-5,0])
    secant._find_root()
    print secant.root
