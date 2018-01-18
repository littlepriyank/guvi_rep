import re
def dig(p): return{'I':1,'i':1,'V':5,'v':5,'X':10,'x':10,'L' :50, 'l':50,'C' :100, 'c':100,'D':500, 'd':500,'M' :1000,'m':1000}[p]
try:
    stl = input("enter a romman number in capitals")
    s = re.match(r'[I|V|X|L|C|D|M|i|v|x|l|c|d|m]*',stl)
    y=len(stl)
    a = [];t=0;skip = 0
    if(s and y<=20):
        for i in range(0,len(stl)):
            a.insert(i,dig(stl[i]))
        for x in range(len(a)-1):
            if(skip==0):
                if(a[x]>=a[x+1]):
                    if(x==len(a)-2):
                        t=t+a[x]+a[x+1]
                    else:
                        t=t+a[x]
                else:
                    t = t+a[x+1]-a[x]
                    skip=1
            else:
                skip=0
        print(t)
    else:
         raise Exception
except:
    print("Invalid Input")
