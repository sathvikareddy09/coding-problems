array=[1,2,5,6]
k=int(input())
i=1 
while(k>0):
    if(i in array):
        i=i+1 
    else:
        k=k-1
        i=i+1 
print(i-1)