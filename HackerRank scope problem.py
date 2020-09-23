n=int(input())
a=str(input())
a=[int(i) for i in a]
if len(a)==n:
    a.sort()
    diff=(a[-1]-a[0])
    print(diff)
else:
    print("Enter a valid input")
