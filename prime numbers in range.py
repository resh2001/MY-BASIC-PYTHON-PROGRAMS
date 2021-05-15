lower=eval(input("enter the lower range " ))
upper=eval(input("enter the upper range " ))
for n in range(lower,upper+1):
    if n>0:
        for i in range(2,n):
            if(n%i)==0:
                break
        else:
            print(n,end=',')
