r = input()
if((r>='a' and r<='z')or(r>='A' and r<='Z')):
	if(r=='a' or r== 'A' or r == 'e' or r == 'E' or r=='i' or r =='I' or r=='o' or r =='O' or r == 'U' or  r =='u'):
		print("Vowel")
	else:
		print("Consonant")
else:
	print("Invalid Input")
