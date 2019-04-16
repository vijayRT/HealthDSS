from opinion import Opinion
import math
class ComplexOperators(object):
    
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
    
    def constraintfusion(self, x, y):
        har = x.b*y.u+y.b*x.u + x.b*y.b
        con = x.b * y.d + y.b*x.d
        if(con == 1):
            return Opinion(0.5, 0.5, 0.5, 0.5)
        u = x.u*y.u/(1-con)
        b = har/(1-con)
        a = (x.a*(1-x.u)+y.a*(1-y.u))/(2-x.u-y.u) if (x.u+y.u<2) else (x.a+y.a)/2
        return Opinion(b, 1 - u - b, u, a)
    
    def cumulativefusion(self, x, y):
        if(x.u!=0 or y.u!=0):
            b=(x.b*y.u+y.b*x.u)/(x.u+y.u-x.u*y.u)
            u=x.u*y.u/(x.u+y.u-x.u*y.u)
            a=(x.a*y.u+y.a*x.u-(x.a+y.a)*x.u*y.u)/(x.u+y.u-2*x.u*y.u) if (x.u!=1 or y.u!=1) else (x.a+y.a)/2
        else:
            b=0.5*(x.b+y.b)
            u=0
            a=0.5*(x.a+y.a)
        return Opinion(b, 1 - u - b, u, a)
    

    def contraposition(self, ygivenx, ygivennotx, ax):
        Px_given_y = ax*ygivenx.p/(ax*ygivenx.p+(1-ax)*ygivennotx.p) if (ax*ygivenx.p+(1-ax)*ygivennotx.p>0) else +(ax*ygivenx.p!=0)
        Px_given_noy = ax*(1-ygivenx.p)/(ax*(1-ygivenx.p)+(1-ax)*(1-ygivennotx.p)) if (ax*(1-ygivenx.p)+(1-ax)*(1-ygivennotx.p) > 0) else +(ax*(1-ygivenx.p)!=0)
    
    
        u_maxi_xy = Px_given_y/ax if (Px_given_y<ax or ax==1) else (1-Px_given_y)/(1-ax)
        u_maxi_xnoy = Px_given_noy/ax if (Px_given_noy<ax or ax==1) else (1-Px_given_noy)/(1-ax)
    
    
        uSyX = ygivenx.u + ygivennotx.u
        wuyx = ygivenx.u/uSyX if (uSyX>0) else +(ygivenx.u!=0)
        wuynox = ygivennotx.u/uSyX if (uSyX>0) else +(ygivennotx.u!=0)
    
        u_maxiyx = ygivenx.p/ygivenx.a if (ygivenx.p<ygivenx.a or ygivenx.a==1) else (1-ygivenx.p)/(1-ygivenx.a)
        u_maxiynox = ygivennotx.p/ygivenx.a if (ygivennotx.p<ygivenx.a or ygivenx.a==1) else (1-ygivennotx.p)/(1-ygivenx.a)
    
        uwyx = wuyx * ygivenx.u/u_maxiyx if (u_maxiyx!=0) else 0
        uwynox = wuynox*ygivennotx.u/u_maxiynox if (u_maxiynox!=0) else 0 
        uwyX = uwyx + uwynox
        vacuous_uxy = uwyX + (1 - abs(ygivenx.p-ygivennotx.p))*(1-uwyX)
        u_x_cp_y = u_maxi_xy*vacuous_uxy
        u_x_cp_noy = u_maxi_xnoy*vacuous_uxy
        b_x_cp_y = Px_given_y - ax*u_x_cp_y
        b_x_cp_noy = Px_given_noy - ax*u_x_cp_noy
        dr1=1-u_x_cp_y-b_x_cp_y
        dr2=1-u_x_cp_noy-b_x_cp_noy
        if(dr1<0):
            b_x_cp_y+=dr1
            dr1=0
        elif( b_x_cp_y<0):
            dr1+=b_x_cp_y 
            b_x_cp_y=0
        
        if( dr1 + b_x_cp_y + u_x_cp_y > 1):
            u_x_cp_y = 1-dr1-b_x_cp_y
        
        if(dr2<0):
            b_x_cp_noy+=dr2
            dr2=0
        elif( b_x_cp_noy<0):
            dr2+=b_x_cp_noy
            b_x_cp_noy=0
        
        if( dr2 + b_x_cp_noy + u_x_cp_noy > 1):
            u_x_cp_noy = 1-dr2-b_x_cp_noy
        o1 = Opinion(b_x_cp_y, dr1, u_x_cp_y, ax)
        o2 = Opinion(b_x_cp_noy, dr2, u_x_cp_noy, ax)
        return o1, o2
    def abduction(self, ygivenx, ygivennotx, y):
        cpygx, cpygnx = self.contraposition(ygivenx, ygivennotx, 0.3)
        return(self.deduction(cpygx, cpygnx, y))