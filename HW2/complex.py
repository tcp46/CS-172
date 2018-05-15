#Tess Porter
#April 26, 2018
#CS 172 - 068

class ComplexNumber:
    
    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)
    
    def __str__(self):
        if self.__y < 0:
            return str(self.__x) + " " + str(self.__y) + "i"
        else:
            return str(self.__x) + " + " + str(self.__y) + "i"
    
    def getReal(self):
        return float(self.__x)
    
    def getImaginary(self):
        return float(self.__y)
    
    def __add__(self, other):
        #operational overload for addition
        new_real = self.getReal() + other.getReal()
        new_imaginary = self.getImaginary() + other.getImaginary()
        return ComplexNumber(new_real, new_imaginary)
    
    def __sub__(self, other):
        #operational overload for subtraction
        new_real = self.getReal() - other.getReal()
        new_imaginary = self.getImaginary() - other.getImaginary()
        return ComplexNumber(new_real, new_imaginary)
    
    def __mul__(self, other):
        #operational overload for multiplication
        new_real = (self.getReal() * other.getReal()) - (self.getImaginary() * other.getImaginary())
        new_imaginary = (self.getReal() * other.getImaginary()) + (self.getImaginary() * other.getReal())
        return ComplexNumber(new_real, new_imaginary)
    
    def __truediv__(self, other):
        #operational overload for division
        new_real = (self.getReal() * other.getReal()) + (self.getImaginary() * other.getImaginary())
        new_real = new_real / (other.getReal() * other.getReal() + other.getImaginary() * other.getImaginary())
        
        new_imaginary = ((0 - self.getReal()) * other.getImaginary()) + (self.getImaginary() * other.getReal())
        new_imaginary = new_imaginary / (other.getReal() * other.getReal() + other.getImaginary() * other.getImaginary())
        
        return ComplexNumber(round(new_real,2), round(new_imaginary,2))
    
    def __pow__(self, exp):
        #operational overload for exponential/power stuff
        if exp == 0:
            x = ComplexNumber(1,0)
            return x
        elif exp == 1:
            return ComplexNumber(self.getReal(), self.getImaginary())
        else:
            temp = ComplexNumber(self.getReal(), self.getImaginary())
            #call the multiplication method and multiply complex number by itself
            for num in range(2, exp+1):
                temp = temp * ComplexNumber(self.getReal(), self.getImaginary())
                num += 1
            return temp
        

if __name__ == "__main__":
    #testing in the class module
    c1 = ComplexNumber(4,3)
    c2 = ComplexNumber(2,8)
    print(c1)
    print(c1 + c2)
    print(c1 * c2)
    print(c1 / c2)
    print(c1 ** 3) 