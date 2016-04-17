import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def pend(y,t,a,b):
    y0,y1 = y
    dydt = [a*(y0-(y0*y1)),b*(-y1+(y0*y1))]
    return dydt
    
if __name__ == "__main__":
    a=1.0
    b=0.2
    y0=[0.1,1.0]
    t = np.linspace(0,5,101)
    sol = odeint(pend,y0,t,args=(a,b))
    print('      y0     |     y1     ')
    print('==========================')
    print(sol)
    
    plt.plot(t,sol[:,0],'b',label='y0(t)')
    plt.plot(t,sol[:,1],'r',label='y1(t)')
    plt.legend(loc='best')
    plt.xlabel('t')
    plt.ylabel('y(t)')
    plt.title('Graph of y(t) against t')
    plt.grid()
    plt.show()