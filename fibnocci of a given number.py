n=int(input('enter the number:  '))
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
