sum=0
a=0
b=1
for i in range (1,100):
	c=a+b
	a,b=b,c
	if c < 4000000:
		if (c%2)==0:
			sum=sum+c
print (sum)

	
