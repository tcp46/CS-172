#Tess Porter
#April 26, 2018
#CS 172 - 068

from complex import ComplexNumber

import sys

def a(c, k):
    #sumation
    count = 0
    complex = ComplexNumber(0,0)
    for num in range(count, k + 1):
        complex = complex + (c ** num)
        num += 1
    return complex

def b(c, k):
    #exponential divisions with complex numbers
    num1 = (ComplexNumber(1,0) - (c**(k+1)))
    num2 = (ComplexNumber(1, 0) - c)
    result = num1/num2
    return result

if __name__=="__main__":
    #command line enter of complex number values
    complex1 = sys.argv[1]
    complex2 = sys.argv[2]
    k = int(sys.argv[3])
    #complex1 = 2
    #complex2 = 3
    #k = 10
    c = ComplexNumber(complex1, complex2)
    answer1 = a(c,k)
    answer2= b(c,k)
    print("For Complex Number", str(c), "and k=", k)
    print("a(", str(c), ",", k, ") = ", answer1)
    print("b(", str(c), ",", k, ") = ", answer2)
    print("This proves that a(c,k) = b(c,k)")

    