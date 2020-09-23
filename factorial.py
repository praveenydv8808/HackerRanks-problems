x=int(input("Enter the no for finding factorial: "))
fact=1
for i in range(1,x+1):
    if i!=0:
        fact=fact*i
print("factoral of {} is {}".format(x,fact))
