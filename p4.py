for i in range (1,1000):
	for j in range (1,1000):
		a=i*j
		num=a
		temp=num
		rev=0
		while(num>0):
		    dig=num%10
		    rev=rev*10+dig
		    num=num//10
		if(temp==rev):
			if a>900000:
				print(a)
		