def decimalToBinary(n):  
    return bin(n).replace("0b", "") 
count=0
for i in range(0,1000000):
	d=str(i)
	e=d[::-1]
	#print(e)
	if d==e:
		f=str(decimalToBinary(i))
		#print(f,i)
		g=f[::-1]
		#print(g)
		if f==g:
			count+=i
			#print(i)
			#count
print(count)