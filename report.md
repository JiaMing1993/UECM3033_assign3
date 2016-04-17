UECM3033 Assignment #3 Report
========================================================

- Prepared by: Khoo Jia Ming
- Tutorial Group: T3

--------------------------------------------------------

## Task 1 --  Gauss-Legendre formula

The reports, codes and supporting documents are to be uploaded to Github at: 

[https://github.com/JiaMing1993/UECM3033_assign3](https://github.com/JiaMing1993/UECM3033_assign3)


First, get the weights and nodes by using numpy.polynomial.legendre.leggauss(n). As there’s two cases could be happened which is case 1, a = -1 ; b=1, and case 2 , a not equal to -1 ; b not equal to 1, therefore if else loop is used. When it is case 1, just use the formula of G(f) = w1*f(x1) + w2*f(x2) + … + wN*f(xN). If it is case 2, use (a+b)/2)+(((b-a)/2) to be the transformation to transform a and b to -1 and 1. Since I am using transformation, the function will have a d/dt. Thus, use (b-a)/2.

I get the weights and nodes by using numpy.polynomial.legendre.leggauss(n). The code is to compute the sample points and weight for Gauss-Legendre quadrature. These sample points and weights will correctly integrate polynomials of degree 2*(n-1) or less over the interval [-1,1] with the weight function f(x) = 1.

---------------------------------------------------------

## Task 2 -- Predator-prey model

Explain how you implement your `task2.py` here, especially how to use `odeint`.

![graph.png](graph.png)
Put your graphs here and explain.

Is the system of ODE sensitive to initial condition? Explain.

-----------------------------------

<sup>last modified: change your date here</sup>
