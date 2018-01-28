import math
try:
    n = int(input())
    c=0
    a=[]
    while(n%2==0):
        n = int(n/2)
        c+=1
    if(c>0):
        c=0
        print(2,end= " ")
    for i in range(3,int(math.sqrt(n))+1,2):
        while(n%i==0):
            n=int(n/i)
            c+=1
        if(c>0):
            c=0
            print(i,end= " ")
    if n>2:
        print(n,end=" ")    
except:
    print("Invalid Input")
