def factors (n):
    factors = []
    x = range (1, n + 1)
    for i in x:
        if (n % i == 0):
          factors.append(i)
          print(i, end=' ')
    print(factors)
  
class Factors:
    def __init__(self):
        self.factors = []
    def __call__(self, n):
      for i in range (1, n + 1):
        if n % i == 0:
            self.factors.append(i)
      return self.factors
      
factors_of = Factors() 
def testdata():
  factors(12)
  factors(100)
def testinput():
  while True:
      n = int(input("What number do you want to FACTORIZE ?!?!"))
      try:
            n = int(n)
            if n <= 0:
                raise ValueError
            print("Factors of {0} is: ".format(n))
            print(factors_of(n))
      except ValueError:
            print(f'Positive integer number is expected, got "{n}" Try again.')

if __name__ == "__main__":
    testinput()
if __name__ == "__main__":
    testdata()