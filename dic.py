n=int(input())
    data={}
    call_name=[]
    for i in range(1,n+1):
        string=str(input())
        hero=string.split()
        data[hero[0]]=hero[1]
    for p in range(1,n+1):
        name=input()
        call_name.append(name)
    for q in range(0,len(call_name)):
        key=call_name[q]
        if key in data:
            print(key+"="+data.get(key))
        else:
            print("Not found")
        

