n=int(input("enter the upper limit"))
print("prime numbers are")
for n in range(0,n+1):
  if n > 0:
        for i in range(2,n):
            if (n%i) == 0:
                break
        else:
             print(n,end=',')
                
