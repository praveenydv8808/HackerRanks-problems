T=int(input())
if T in range(1,11):
    for k in range(1,T+1):
        S=str(input())
        p=len(S)
        even=""
        odd=""
        for i in range(0,p):
            if i==0 or i%2==0:
                even.append(S[i])
            else:
                odd.append(S[i])
        print(even + " " + odd);


