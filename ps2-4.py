try:
    s = input()
    q=""
    for i in range(len(s)):
        if(s[len(s)-1-i] not in ['a','e','i','o','u','A','E','I','O','U']):
            q=q+s[len(s)-1-i]
    print(q)        
except:
    print("Invalid Input")
