try:
    p,q = [x for x in input().split(" ")]
    j=0;c=0
    if((len(p)and len(q))<=100000):
        if(len(p)==len(q)):
            for i in p:
                if(i==q[j]):
                    j+=1
                else:
                     j+=1
                     c+=1
                if(c>1):
                      print("NO")
                      break
            if(c==1):
                 print("yes")         
except:
    print("Invalid Input")
