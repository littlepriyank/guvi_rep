try:
    s = input("enter a string")
    if(len(s)<=100000):
        print(s[::-1])
    else:
        raise Exception
except:
    print("Invalid")
