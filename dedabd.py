from opinion import Opinion
import math
class DedAbd(object):
    
    def __init__(self):
        pass

    def deduction(self, y_x, y_notx, x):
        bIy = x.b * y_x.b + x.d * y_notx.b + x.u * (y_x.b * x.a + y_notx.b * (1-x.a))
        dIy = x.b * y_x.d + x.d * y_notx.d + x.u * (y_x.d * x.a + y_notx.d * (1-x.a))
        uIy = x.b * y_x.u + x.d * y_notx.u + x.u * (y_x.u * x.a + y_notx.u * (1-x.a))
        Pyvacuousx = y_x.b * x.a + y_notx.b * (1-x.a) + y_x.a * (y_x.u * x.a+y_notx.u * (1-x.a))
        

        if (((y_x.b>y_notx.b) and (y_x.d>y_notx.d)) or ((y_x.b<=y_notx.b) and (y_x.d<=y_notx.d))):
            k=0
        elif ((y_x.b>y_notx.b) and (y_x.d<=y_notx.d)):
            if(Pyvacuousx<=(y_notx.b+y_x.a * (1-y_notx.b-y_x.d))):
                if(x.p<=x.a):
                    k=x.a * x.u * (bIy - y_notx.b)/(y_x.a * x.p)
                else:
                    k=x.a * x.u * (dIy - y_x.d) * (y_x.b-y_notx.b)/((x.d+(1-x.a) * x.u) * y_x.a * (y_notx.d-y_x.d))
            else :
                if(x.p<=x.a):
                    k=(1-x.a) * x.u * (bIy -y_notx.b) * (y_notx.d-y_x.d)/(x.p * (1-y_x.a) * (y_x.b-y_notx.b))
                else:
                    k=(1-x.a) * x.u * (dIy-y_x.d)/((1-y_x.a) * (x.d+(1-x.a) * x.u))
        else :
            if(Pyvacuousx<=(y_notx.b+y_x.a * (1-y_notx.b-y_x.d))):
                if(x.p<=x.a):
                    k=(1-x.a) * x.u * (dIy-y_notx.d) * (y_notx.b-y_x.b)/(x.p * y_x.a * (y_x.d-y_notx.d))
                else:
                    k=(1-x.a) * x.u * (bIy-y_x.b)/(y_x.a * (x.d+(1-x.a) * x.u))
            else :
                if(x.p<=x.a):
                    k=x.a * x.u * (dIy-y_notx.d)/(x.p * (1-y_x.a))
                else:
                    k=x.a * x.u * (bIy-y_x.b) * (y_x.d-y_notx.d)/((1-y_x.a) * (y_notx.b-y_x.b) * (x.d+(1-x.a) * x.u))
                
            
        if(math.isnan(k)):
            k = 0
        
        
        by = bIy - y_x.a * k
        dy = dIy - (1-y_x.a) * k
        uy = uIy + k
        
        return(Opinion(belief=by, disbelief=dy, uncertainty=uy, baserate=y_x.a))