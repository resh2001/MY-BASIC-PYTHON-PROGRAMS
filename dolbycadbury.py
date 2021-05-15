def TotalCount(P,Q,R,S):
  count=0
  for l in range(P,Q+1):
    for b in range(R,S+1):
      count += CountPerChocolateBar(l,b)
      return count
def CountPerChocolateBar(l,b):
  count=0
  while True:
    longer=max(l,b)
    shorter=min(l,b)
    count+=1
    diff=longer-shorter
    if diff==0:
      return count
    else:
      l=min(l,b)
      b=diff
    while True:
      numbers=raw_input("Number: ")
      P= int(numbers.split()[0])
      Q= int(numbers.split()[1])
      R= int(numbers.split()[2])
      S= int(numbers.split()[3])
      tc= TotalCount(P,Q,R,S)
      print(tc)
