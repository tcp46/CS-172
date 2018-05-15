from fraction import Fraction

#Harmonic Series
def H(n):
    frac = Fraction(1,1)
    k = 2
    while k <= n:
        frac = frac + Fraction(1,k)
        k += 1
    return frac

#Two
def T(n):
    frac = Fraction(1,1)
    k = 1
    while k <= n:
        frac = frac + (Fraction(1,2) ** k)
        k += 1
    return frac

#Zero
def Z(n):
    frac = Fraction(1,1)
    k = 1
    while k <= n:
        frac = frac + (Fraction(1,2) ** k)
        k += 1
    return Fraction(2,1) - frac

#Partial Riemann Zeta
def R(n, b):
    frac = Fraction(1,1)
    k = 2
    while k <= n:
        frac = frac + (Fraction(1,k) ** b)
        k += 1
    return frac

print('Welcome to Fun with Fractions!')

valid = True
while valid == True:
    i = input('Enter Number of iterations (integer>0):\n')
    try:
        i = int(i)
        if i > 0:
            valid = False
        else:
            valid = True
    except ValueError as e:
        valid = True

print('H({})='.format(i), H(i))
print('H({})~='.format(i), H(i).approximate())
print('T({})='.format(i), T(i))
print('T({})~='.format(i), T(i).approximate())
print('Z({})='.format(i), Z(i))
print('Z({})~='.format(i), Z(i).approximate())

for num in range(2, 9):
    print('R({})='.format(i, num), R(i, num))
    print('R({})~='.format(i,num), R(i, num).approximate())