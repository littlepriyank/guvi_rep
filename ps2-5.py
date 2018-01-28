try:
    import re
    s = input()
    a=[0]*26
    match = re.match("^([a-zA-Z]+)( [a-zA-Z]+)*$",s)
    if(match):
        for i in range(len(s)):
            if(s[i]!=' '):
                if(ord(s[i])>96):
                    a[ord(s[i])-97]+=1
                else:
                    a[ord(s[i])-65]+=1
        x=a.index(max(a))
        print(chr(x+97))
    else:
        raise Exception
except:
    print("Invalid Input")
