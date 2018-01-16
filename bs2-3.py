N = int(input("enter a number"))
if(N<=1000):
    c=0
    for i in range(2,int(N/2)+1):
        if(N%i==0):
            c=1
            break
    if(c==0):
        print("yes")
    else:
        print("no")
