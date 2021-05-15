r=int(input('enter the value of r: '))
print('area of circle "A" is ',3.14*r*r)
x=int(input('enter the value of x :'))
y=int(input('enter the value of y :'))
x+=y
print('x+=y',x)
x-=y
print('x+=y',x)
x*=y
print('x*=y',x)
x/=y
print('x/=y',x)
x%=y
print('x%=y',x)
x**=y
print('x**=y',x)
x//=y
print('x//=y',x)
str1=input('enter your name:  ')
str2=input('enter your age:  ')
str3=input('enter your address:  ')
str4=input('enter your education: ')
print('name is  ',str1)
print('age is  ',str2)
print('address is  ',str3)
print('education is  ',str4)
print("x==y",x==y)
print("x!=y",x!=y)
print("x>y",x>y)
print("x<y",x<y)
print("x<=y",x<=y)
print("x>=y",x>=y)
n=int(input('enter the value of n : '))
i=0
f=1
if(n==0):
   print("The factorial of 0 is 1")
else:
   for i in range(1,n+1):
        f=f*i
   print("The factorial of",n,"is",f)
f1=0
f2=1
f=1
if(n<=0):
    print('enter the positive integer')
elif(n==1):
    print('fibnocci sequence upto',n,':')
    print(f1)
else:
    print('fibnocci sequence upto',n,':')
    while (f<=n):
      print(f1,end=',')
      f=f1+f2
      f1=f2
      f2=f
      f+=0
def mul(x):
   return 4*x
def add(y):
   return 5+y
def sub(z):
   return 6*z
def div(a):
   return 6/a
print(mul(2))
print(mul(3))
print(add(2))
print(add(3))
print(sub(2))
print(sub(3))
print(div(2))
print(div(3))
def hi():
    print('hi hello welcome')
hi()
hi()
def hi(country='India'):
   print("iam from "+country)
hi("Norway")
hi("US")
hi()
year=int(input('enter the year:  '))
if(year%4==0 and year%100!=0 or year%400==0):
    print('the given year is a leap year')
else:
    print('the given year is not a leap year')
print("x<5 and y>5",(x<5 and y>5))
print("x<5 or y>5",(x<5 or y>5))
print("not x<5<y",(not( x<5<y)))
a=int(input('enter the value of a '))
b=int(input('enter the value of b '))
c=int(input('enter the value of c '))
if(a>b)&(a>c):
    print('a is greater than b and c')
elif(b>c):
        print('b is greater than a and c')
elif(a==b==c):
        print('a,b,c all the values are equal')
else:
        print('c is greater than a and b')
x=('reshma')
print("a in x:  ","a" in x)
print("l in x:  ","l" in x)
string1='Reshma'
string2=' Ramesh'
string3=' Uthra'
string4=' !'
print('Hai '+string1 +string2 +string3+ string4)
a=int(input('enter the value of a:  '))
if(a%2)==0:
    print("{0} is even number".format(a))
else:
    print("{0} is odd number".format(a))
x=y=1
xy='hai welcome'
print(x,y,xy)
import cmath
a=float(input('enter a:  '))
b=float(input('enter b:  '))
c=float(input('enter c:  '))
d=b*b-4*a*c
r1=(-b+cmath.sqrt(d)/(2*a))
r2=(-b-cmath.sqrt(d)/(2*a))
print('the roots are {0} and {1}'.format(r1,r2))
x=5
for x in range (10):
   print(x)
print('sum=',a+b)
print('difference=',a-b)
print('multiplication=',a*b)
print('division=',a/b)
print('modulous=',a%b)
print('first number is',a)
print('second number is',b)
a=int(input('enter the value of a '))
b=int(input('enter the value of b '))
c=a
a=b
b=c
print('the value of "a" after swapping:{}'.format(a))
print('the value of "b" after swapping:{}'.format(b))
x=int(input('enter the value of x: '))
y=int(input('enter the value of y: '))
a=y if (x<y) else x
print("the output is ",a)
