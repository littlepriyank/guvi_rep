N,Q = [int(x) for x in input().split()]
if(N<=1000 and Q<=1000):
    for i in range(N+1,Q):
        c=0
        for x in range(2,int(i/2)+1):
            if(i%x==0):
                c=1
                break
        if(c==0):
            print(i,end=" ")
