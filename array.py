import numpy
n=int(input())
string=str(input())
arr=[]
arr=string.split()
arr.reverse()
for i in range(n):
    print(arr[i],end=" ")
    
