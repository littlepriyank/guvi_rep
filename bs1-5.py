a = int(input())
b = int(input())
c = int(input())
if(a>=b):
	if(a>=c):
		print("largest is ",a)
	else:
		print("largest is ",c)
elif(b>=c):
	print("largest is ",b)
else:
	print("largest is ",c)