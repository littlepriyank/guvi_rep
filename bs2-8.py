N,Q = [int(x) for x in input().split()]
for i in range(N+1,Q):
    x=i;p = [];j=0;a=0;l=0
    while(x!=0):
        p.insert(j,x%10)
        j+=1
        x=int(x/10)
    for t in p:
        a=a+t**j
    if(a==i):
        print(i,end=' ')
    
