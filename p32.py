d="123456789"
c=[]
f=[]
for i in range(1,100):
	for j in range(1,2000):
		a=i*j
		b=str(i)+str(j)+str(a)
		e=sorted(b)
		b= "".join(e)
		
		#print(b)
		
			
		if b==d :
			if a in c:
				pass
			else:

				c.append(a)
print(c)
print(sum(c))

