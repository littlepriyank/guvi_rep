n = int(input("enter a number"))
if(n<=100000):
    c=0;x=n;p = [];i=0
    while(x!=0):
        p.insert(i,x%10)
        i+=1
        x=int(x/10)
    for j in p:
        c=c+j**i
    if(c==n):
        print("yes")
    else:
        print("no")
