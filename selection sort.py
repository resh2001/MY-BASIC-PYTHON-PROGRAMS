def selectionsort(alist):
    for i in range(len(alist)-1,0,-1):
        POS=0
        for location in range(1,i+1):
            if alist[location]>alist[POS]:
             POS=location
        temp=alist[i]
        alist[i]=alist[POS]
        alist[POS]=temp
alist=[54,26,93,17,77,44,55,20]
selectionsort(alist)
print(alist)
