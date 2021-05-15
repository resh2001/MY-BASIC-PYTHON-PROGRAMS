n=int(input('enter the value of n : '))
i=0
f=1
if(n==0):
   print("The factorial of 0 is 1")
else:
   for i in range(1,n+1):
        f=f*i
   print("The factorial of",n,"is",f)
