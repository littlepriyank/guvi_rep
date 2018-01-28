try:
    n,k = [int(x) for x in input().split(" ")]
    a = list(map(int,input().split(' ')))
    b= [0]*(2*n)
    for i in range(n):
        b[i] = a[i]
        b[n+i] = a[i]
    c=abs(n-k)
    print(c,b[c:c+n])
except:
    print("Invalid Input")
