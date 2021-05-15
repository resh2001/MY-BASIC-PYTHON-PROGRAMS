import math
def newtonsqrt(n,howmany):
    approx=0.5*n
    for i in range(howmany):
        betterapprox=0.5*(approx+n/approx)
        approx=betterapprox
        print("square root at",i,"iteration",betterapprox)
        print("square root with newton's method",betterapprox)
        print("square root without newton's method",math.sqrt(n))
