import cmath
a=float(input('enter a:  '))
b=float(input('enter b:  '))
c=float(input('enter c:  '))
d=b*b-4*a*c
r1=(-b+cmath.sqrt(d)/(2*a))
r2=(-b-cmath.sqrt(d)/(2*a))
print('the roots are {0} and {1}'.format(r1,r2))



