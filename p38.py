a="123456789"

for i in range(9999,9000,-1):
	b=str(i*1)
	c=str(i*2)
	d=b+c
	e=d
	e=sorted(e)
	e = ''.join(e)
	if e==a:
		print(d)
		break



