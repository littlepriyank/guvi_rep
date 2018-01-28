try:
    n = int(input())
    s=0
    while(n!=0):
        l = n%10
        s = s+l*l
        n= int(n/10)
    print(s)    
except:
    print("Invalid Input")
