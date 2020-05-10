sum=2
a=1
b=1
for i in range(1,1000000):
	c=(a+b)
	d=str(c)
	#print(type(d))
	a,b=b,c

	sum+=1
	if len(d) == 1000:
		print(sum)
		print(d)
		break