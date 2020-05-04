



def fact(n):
	p=1
	for i in range(1,n+1):
		p=p*i
		#print(i)
	return p
c=int(input("enter"))
d=2*c
e=(fact(d))/(fact(c)*fact(c))
print(e)
