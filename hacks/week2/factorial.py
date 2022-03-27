# fibonacci_class.py

class Factorial:
    def __init__(self):
        self.factorial = [1, 1]
      
    def __call__(self, n):
        if n < len(self.factorial):
            return self.factorial[n]
        else:
            # Compute the requested Factorial number
            factorial_number = n* self(n - 1) 
            self.factorial.append(factorial_number)
        return self.factorial[n]


def tester():
    # Make a factorial object
    while True:
        factorial_of = Factorial()
        n = input("Enter the number of terms: ")
        try:
            n = int(n)
            # Validate the value of n
            if n <=0:
                raise ValueError
            # Factorial term corresponding to n
            print(f"Term {n} of Factorial sequence is: ", factorial_of(n - 1))
            # Produces a list of factorial values, one factorial result for each step in range
            print(f"Factorial sequence of {n} terms is: ", [factorial_of(i) for i in range(n)])
            break
        except ValueError:
            print(f'Positive integer number expected, got "{n}" Try again.')


if __name__ == "__main__":
   tester()
