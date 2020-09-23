number=int(input())
arr=[]
if 1<=number and number<=10*6:
    binary=bin(number)
    arr=binary.split()
k=1
for i in range(2,len(arr)):
    if arr[i]==1:
        k=k+1
    else:
        print(k)
                    
