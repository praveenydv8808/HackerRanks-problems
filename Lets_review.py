n=int(input())
data=[]
even=[]
odd=[]
for i in range(1,n+1):
    string=str(input())
    Hero=string.split()
    for e in range(len(Hero)):
        if e%2==0:
            even.append(Hero[e])
        else:
            odd.append(Hero[e])
        for k in range(len(even)):
            print(even[k],end="")
        
            
    
    

    
