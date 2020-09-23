n=int(input())
arr=[]
def insert(i,e):
    arr.insert(i,e)
def printx():
    print(arr)
def sort():
    arr.sort()
def pop():
    arr.pop(arr[len(arr)-1])
def reverse():
    arr.reverse()
for m in range(1,n+1):
    x=input()
    hero=x.split()
    if hero[0]=="insert":
        i=int(hero[1])
        e=int(hero[2])
        insert(i,e)
    elif hero[0]=="remove":
        e=int(hero[1])
        arr.remove(e)
    elif hero[0]=="append":
        e=int(hero[1])
        arr.append(e)
    elif hero[0]=="print":
        printx()
    elif hero[0]=="sort":
        sort()
    elif hero[0]=="pop":
        pop()
    elif hero[0]=="reverse":
        reverse()
    



