for i in range (1,1000):
	a=i*i
	for j in range (i+1,1000):
		b=j*j
		for k in range (j+1,1000):
			c=k*k
			if a<b<c:
				if a+b == c:
					if i+j+k == 1000:
						print(i,j,k)
						print(i*j*k)
						print(a,b,c)
