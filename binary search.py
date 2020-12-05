def bsearch(alist,item):
    first = 0
    last = len(alist)-1
    found = False
    while(first<=last and not found):
        mid = (first + last)//2
        if alist[mid] == item:
            found = True
            print("the element found in the position ",mid)
        else:
            if item < alist[mid]:
                 last = mid - 1
            else:
                 first = mid + 1
    return found
a=[]
n=int(input("enter the upper limit"))
for i in range(0,n):
    e=int(input("enter the elements"))
    a.append(e)
x=int(input("enter the elements to be searched"))
c=bsearch(a,x)
print(c)
