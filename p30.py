a=[]

for i in range(2,400000):
	d=0
	e=i
	while e>0:

		j=e%10
		#print(j,"j")
		d=d+j**5
	#print(d)
		#print(d)
		e=int(e/10)
	#print(d,i)
	if i == d:
		a.append(i)
	else:
		pass
print(sum(a))
print(a)





