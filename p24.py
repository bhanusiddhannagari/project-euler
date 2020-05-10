from itertools import permutations
count=0 
x=permutations("0123456789")
for i in x:
	count+=1
	if count==1000000:
		print(str(i))
		break