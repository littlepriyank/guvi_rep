s = input("enter a string")
a = list(s)
b=''
for i in range(0,len(s)-1,2):
    t=a[i]
    a[i]=a[i+1]
    a[i+1]=t
    b = b+a[i]+a[i+1]
if(len(a)%2!=0):    
    b= b+a[i+2]    
print(b)    
