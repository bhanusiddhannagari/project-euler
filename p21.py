
d=0
for i in range (0,10001,2):
	a=0
	b=0
	for j in range (1,i):
	 	if i%j==0:
	 		a+=j
	for k in range (1,a):
	
		if a%k==0:
			b+=k
	#print(b,a,"a")
	if b==i and b!=a:
		d+=i
		#print(b,a,"a")

		#print(a,"i",i)
print(d)
