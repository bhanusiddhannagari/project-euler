counter=2
n=10001
for i in range (3, n**2, 2):
	#print(i)
	k=1
	#print(i,"i")
	while k*k < i:
		k += 2
		#print(k,"k")
		if i % k == 0:
			break
	else:
		counter += 1
		#print(i)
	if counter == n:
		print(i)
	
		break


