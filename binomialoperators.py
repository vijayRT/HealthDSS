from decimal import *
from opinion import Opinion

getcontext().prec = 2
class BinomialOperators:
    def __init__(self):
        pass

    def addition(self, x, y):
        b = x.b + y.b
        a = x.a + y.a
        d = (((x.a * (x.d - y.b)) + (y.a * (y.d - x.b))) / a)
        u = (((x.a * x.u) + (y.a * y.u)) / a)
        return Opinion(belief=b, disbelief=d, uncertainty=u, baserate=a)
         
    def subtraction(self, xuy, y):
        b = xuy.b - y.b
        d = ((xuy.a * (xuy.d + y.b)) - (y.a * (1 - y.b - xuy.b - y.u)) / (xuy.a - y.a))
        u = (((xuy.a * xuy.u) - (y.a * y.u)) / xuy.a - y.a)
        a = xuy.a - y.a
        return Opinion(belief=b, disbelief=d, uncertainty=u, baserate=a)
        
    def complement(self, x):
        b = 1 - x.d
        d = 1 - x.b
        u = x.u
        a = 1 - x.a
        return Opinion(belief=b, disbelief=d, uncertainty=u, baserate=a)
         
    def multiplication(self, x, y):
        temp = ((((1 - x.a) * y.a * x.b * y.u) + ((1 - y.a) * x.a * y.b * x.u)) / (1 - x.a * y.a))
        b = (x.b * y.b) + temp
        d = x.d + y.d - (x.d * y.d)
        temp2 = ((((1 - y.a) * x.b * y.u) + ((1 - x.a) * y.b * x.u)) / (1 - x.a * y.a))
        u = (x.u * y.u) + temp2
        a = (x.a * y.a)
        return Opinion(belief=b, disbelief=d, uncertainty=u, baserate=a)
    
    def comultiplication(self, x, y):
        temp1 = ((((1 - y.a) * x.a * x.d * y.u) + ((1 - x.a) * y.a * y.d * x.u)) / (x.a + y.a - (x.a * y.a)))
        temp2 = ((y.a * x.d * y.u) + (x.a * x.u * y.d)) / (x.a + y.a - (x.a * y.a))
        b = x.b + y.b - (x.b * y.b)
        d = (x.d * y.d) + temp1
        u = (x.u * y.u) + temp2
        a = x.a + y.a - (x.a * y.a)
        return Opinion(belief=b, disbelief=d, uncertainty=u, baserate=a)

    def division(self, x, y):
        if not x.a < y.a:
            print("Base Rate Constraint not satisfied")
            return None
        if not x.d >= y.d:
            print("Disbelief Constraint not satisfied")
            return None
        b_constraint = (x.a * (1 - y.a) * (1 - x.d) * y.b) / ((1 - x.a) * y.a * (1 - x.d))
        u_constraint = (((1 - y.a) * (1 - x.d) * y.u) / ((1 - x.a) * (1 - y.d)))
        if not x.b >= b_constraint:
            print("Belief Constraint not satisfied")
            return None
        if not x.u >= u_constraint:
            print("Uncertainty Constraint not satisfied")
            return None
        b = (((y.a * (x.b + x.a * x.u)) / ((y.a - x.a) * (y.b + y.a * y.u))) - ((x.a * (1 - x.d)) / ((y.a - x.a) * (1 - y.d))))
        d = (x.d - y.d) / (1 - y.d)
        u = (((y.a * (1 - x.d)) / ((y.a - x.a) * (1 - y.d))) - ((y.a * (x.b + x.a * x.u)) / ((y.a - x.a) * (y.b + y.a * y.u))))
        a = x.a / y.a
        return Opinion(belief=b, disbelief=d, uncertainty=u, baserate=a)
    
    def codivision(self, x, y):
        if not x.a > y.a:
            print("Base Rate Constraint not satisfied")
            return None
        if not x.b >= y.b:
            print("Belief Constraint not satisfied")
            return None
        d_constraint = (((1 - x.a) * y.a * (1 - y.b) * y.d)/(x.a* (1 - y.a) * (1 - y.b)))
        u_constraint = ((y.a * (1 - x.b) * y.u ) / (x.a * (1 - y.b)))
        if not x.d >= d_constraint:
            print("Disbelief Constraint not satisfied")
            return None
        if not x.u >= u_constraint:
            print("Uncertainty constraint not satisfied")
            return None
        b = ((x.b - y.b) / (1 - y.b))
        d = ((((1 - y.a)* (x.d + ((1 - x.a) * x.u))) / ((x.a - y.a) * (y.d + ((1 - y.a)* y.u)))) - (((1 - x.a) * (1 - x.b)) / ((x.a - y.a) * (1 - y.b))))
        u = (((1 - y.a) * (1 - x.b)) / ((x.a - y.a) * (1 - y.b))) - (((1 - y.a) * (x.d + (1 - x.a) * x.u)) / ((x.a - y.a) * (y.d + (1 - y.a) * y.u)))
        a = (x.a - y.a) / (1 - y.a)
        return Opinion(belief=b, disbelief=d, uncertainty=u, baserate=a)