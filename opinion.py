from decimal import *
class Opinion(object):
    def __init__(self, belief=None, disbelief=None, uncertainty=None, baserate=None):
        TWOPLACES = Decimal(10) ** -2
        self.b = self.limit(belief) if belief is not None else self.limit(1 - disbelief - uncertainty)
        self.d = self.limit(disbelief) if disbelief is not None else self.limit(1 - belief - uncertainty)
        self.u = self.limit(uncertainty) if uncertainty is not None else self.limit(1 - belief - disbelief)
        self.a = self.limit(baserate)
        self.p = self.b + self.u * self.a

    def __str__(self):
        return ("b: {0:.2f}, d: {1:.2f}, u: {2:.2f}, a: {3:.2f}, p: {4:.2f}".format(self.b, self.d, self.u, self.a, self.p) )

    def limit(self, num, minimum=0, maximum=1):
        return max(min(num, maximum), minimum)
