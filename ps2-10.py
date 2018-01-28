try:
    import re
    s = input()
    match = re.match("^[a-zA-Z]+$",s)
    if(match):
        for i in range(len(s)):
            if(ord(s[i])>119 and ord(s[i])<123):
                print(chr(ord(s[i])-23), end = "")
            elif(ord(s[i])>86 and ord(s[i])<91):
                print(chr(ord(s[i])-23),end = "")
            else:
                print(chr(ord(s[i])+3),end = "")
    else:
        raise Exception
except:
    print("Invalid Input")
