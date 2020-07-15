
class Calculus:
    
    def __init__(self):
		print("Calculus class initiated ")


    def newton_method(self,f,df,x0,epsilon,max_iter):
		xn = x0
		for n in range(0,max_iter):
			fxn = f(xn)
			if abs(fxn) < epsilon:
				return "Solution found : {}".format(xn)
			Dfxn = df(xn)
			if Dfxn == 0:
				return "Zero Derivative: Solution Not Found !"
			xn = xn - fxn/Dfxn
			
		return 'Exceeded maximum iterations. No solution found.'

