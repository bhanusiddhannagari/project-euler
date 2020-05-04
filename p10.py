counter=2

a=5
for i in range (3, 10, 2):
	print(i)
	k=1
	#print(i,"i")
	while k*k < i:
		k += 2
		print(k,"k")
		if i % k == 0:
			break
	else:
		counter += 1
		#print(i)
		a+=i
print(a,"a")
"""		#print(i,"i")
#print(counter,"counter")
		
	if counter == n and i < 2000000:
		#print(a,"a")
		#print(i,"i")
		
		print(i)
		print(a)
		break"""


