N = int(input("enter a number"))
if(N<=1000):
    p = 0;x=N
    while(x!=0):
        p = p*10 + x%10
        x=int(x/10)
    if(p==N):
        print("yes")
    else:
        print("no")
