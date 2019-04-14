from decimal import *
getcontext().prec = 2
class Opinion(object):
    def __init__(self, belief=None, disbelief=None, uncertainty=None, baserate=None):
        TWOPLACES = Decimal(10) ** -2
        self.b = Decimal(self.limit(belief)).quantize(TWOPLACES) if belief is not None else Decimal(1 - disbelief - uncertainty) 
        self.d = Decimal(self.limit(disbelief)).quantize(TWOPLACES) if disbelief is not None else Decimal(1 - belief - uncertainty)
        self.u = Decimal(self.limit(uncertainty)).quantize(TWOPLACES) if uncertainty is not None else Decimal(1 - belief - uncertainty) 
        self.a = Decimal(self.limit(baserate)).quantize(TWOPLACES)
        self.p = self.b + self.u * self.a

    def __str__(self):
        return ("b: {}, d: {}, u: {}, a: {}, p: {}".format(self.b, self.d, self.u, self.a, self.p) )

    def limit(self, num, minimum=0, maximum=1):
        return max(min(num, maximum), minimum)
