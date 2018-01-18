try:
        s1,s2 = [x for x in input().split()]
        def isom(s1,s2):
                if(len(s1)!=len(s2)):
                        return False
                a=[False]*256
                b=[-1]*256
                for i in range(len(s1)):
                        if(b[ord(s1[i])]==-1):
                                if(a[ord(s2[i])]):
                                        return False
                                a[ord(s2[i])] = True
                                b[ord(s1[i])] = s2[i]
                        elif(b[ord(s1[i])]!=s2[i]):
                                return False
                return True
        if(isom(s1,s2)):
                print("yes")
        else:
                print("no")
except:
        print("Invalid Input")
