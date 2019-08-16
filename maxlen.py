n1=int(input())
n2=int(input())

arr=[]
max_len=0

for i in range(n1,n2+1):
    arr.append(i)
    while i>1:
        if(i%2==0):
            i=i/2
            arr.append(int(i))
        else:
            i=i*3+1
            arr.append(int(i))
    l=len(arr)    
    if(l>max_len):
        max_len=l
    arr.clear()
    
print(max_len) 

