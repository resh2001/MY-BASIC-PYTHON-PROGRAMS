n=eval(input("enter the number:"))
for i in range(2,n):
    if(n%i==0):
        print("the number is not a prime")
        break
else:
    print("the number is a prime")
