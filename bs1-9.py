N = int(input("enter value of N"))
a = [0]*50;s=0
print("enter the integers of array")
for i in range(0,N):
	a[i] = int(input())
K = int(input("enter the value of K"))
for i in range(0,K):
		s+=a[i]
print(s)		
