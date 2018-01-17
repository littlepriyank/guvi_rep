try:
    N = int(input("enter a number"))
    f=N;r=0
    while(f!=0):
        r=r*10+f%10
        f=int(f/10)
    print(r)    
except:
    print("Invalid Input")
