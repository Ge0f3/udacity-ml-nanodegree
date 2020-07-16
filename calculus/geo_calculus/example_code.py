from calculusG import Calculus

CA = Calculus()
p = lambda x: x**3 - x**2 - 1
Dp = lambda x: 3*x**2 - 2*x
approx = CA.newton_method(p,Dp,1,1e-10,20)
print(approx)