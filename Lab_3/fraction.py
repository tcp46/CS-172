class Fraction:
    #Constructor. Puts fraction in simplest form
    def __init__(self,a,b):
        self.num = a
        self.den = b
        self.simplify()
    #Print Fraction as a String
    def __str__(self):
        if self.den==1:
            return str(self.num)
        else:
            return str(self.num)+"/"+str(self.den)
    #Get the Numerator
    def getNum(self):
        return self.num
    #Get the Denominator
    def getDen(self):
        return self.den
    #Give Numerical Approximation of Fraction
    def approximate(self):
        return self.num/self.den
    #Simplify fraction
    def simplify(self):
        x = self.gcd(self.num,self.den)
        self.num = self.num // x
        self.den = self.den // x
    #Find the GCD of a and b
    def gcd(self,a,b):
        if b==0:
            return a
        else:
            return self.gcd(b,a % b)
    
    #Complete these methods in lab
    #Overloaded operators
    def __add__(self,other):
        return Fraction(self.num * other.den + other.num * self.den, self.den * other.den)
    def __sub__(self,other):
        return Fraction(self.num * other.den - other.num * self.den, self.den * other.den)
    def __mul__(self,other):
        return Fraction((self.num * other.num), (self.den * other.den))
    def __truediv__(self,other):
        return Fraction((self.num * other.den), (self.den * other.num))
    def __pow__(self,exp):
        if exp == 0:
            return Fraction(1,1)
        elif exp < 0:
            return Fraction(self.den ** exp, self.num ** exp)
        else:
            return Fraction(self.num ** exp, self.den ** exp)