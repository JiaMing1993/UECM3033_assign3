import numpy as np
import sympy as sy
#Your optional code here
#You can import some modules or create additional functions

# DO NOT CHANGE THE NAME OF gausslegendre() function
def gausslegendre(f, a, b, n=20):
    ans = 0
    x,w = np.polynomial.legendre.leggauss(n);    
    i=0
    #case 1
    if(a==-1 & b==1):
        while(i<n):
            ans = ans + w[i]*f(x[i])
            i=i+1
            
    #case 2
    else:
        while(i<n):
            #(a+b)/2)+(((b-a)/2) is used to transform a and b to a=-1 and b=1
            temp = ((a+b)/2)+(((b-a)/2)*x[i])
            #(b-a)/2 is used as d/dt of the transformation 
            ans = ans + w[i]*f(temp)*((b-a)/2)
            i=i+1
    return ans

if __name__ == "__main__":
    def f(x):
        return (x**2 +7*x)/(1 +np.sqrt(x))**4
    
    def my_integral():
        x = sy.Symbol('x')
        ans = sy.integrate((x**2 +7*x)/(1 +sy.sqrt(x))**4, (x,0, 1))
        return ans
    
    print('Answer:                    I = ', my_integral())
    print('Your implementation gives: I = ', gausslegendre(f, 0,1))
