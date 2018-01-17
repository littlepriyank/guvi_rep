try:
    N = int(input("enter a number"))
    f=1
    if(N<=20):
        for i in range(1,N+1):
            f=f*i
        print(f)
    else:
        raise Exception
except:
    print("Invalid Input")
