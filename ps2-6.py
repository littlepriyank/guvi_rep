try:
    n = int(input())
    a = list(map(int,input().split(' ')))
    b = [0]*50
    for i in range(n):
        b[a[i]]+=1
    print(b.index(1))    
except:
    print("Invalid Input")
