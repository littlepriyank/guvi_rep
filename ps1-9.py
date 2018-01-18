try:
    l,r = [int(x) for x in input("enter range").split()]
    if(l<=r<=100000):
        a=[True]*(r+1)
        i=2
        while(i*i<=r):
            if(a[i]==True):
                for x in range(i*2,r+1,i):
                    a[x] = False
            i+=1 
        for x in range(l,r+1):
            if(a[x]):
                print(x,end = " ")
    else:
         raise Exception
except:
    print("Invalid Input")
