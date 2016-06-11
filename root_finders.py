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


if __name__ == "__main__":
    bisection = Bisection([(1,3), (1,2), (1,1),-2], [-1,1])
    bisection._find_root()
