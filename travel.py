import numpy as np 
from array import array 

n=int(input("Number of Students:\n"))
arr = list()
expense=0
for i in range(n):
    i=float(input())
    arr.append(i)

print(arr)  
avg=sum(arr)/len(arr)
print(float(avg))


for i in arr:
    if(i!=avg):
        rem=float(avg)-i
        if(rem<0):
            expense+=rem
    else:
        continue
print("Total expense is:",abs(expense))  
  
