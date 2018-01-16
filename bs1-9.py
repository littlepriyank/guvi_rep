N,K = [int(x) for x in input("enter value of N and K").split()]
a = [0]*50;s=0
print("enter the integers of array")
t = input().split()
if(len(t)==N):
    for i in range(N):
        a[i] = int(t[i])
    for i in range(0,K):
        s+=a[i]
    print(s)		
else:
    print("number of integer not equal to N")
