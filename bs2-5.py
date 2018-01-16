N,Q = [int(x) for x in input().split()]
if(N<=100000 and Q<=100000):
    if(N%2!=0):
        N=N+1
    else:
        N=N+2
    for i in range(N,Q,2):
        print(i,end=' ')
