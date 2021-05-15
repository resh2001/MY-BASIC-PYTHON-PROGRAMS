list=[4,1,2,3,5]
count=0
search=int(input("enter the search number: "))
for i in range (0,len(list)):
    if search==list[i]:
        print(str(search)+'found at position'+str(i))
        count=1
        break
    if count==0:
        print("element notfound in a list")
