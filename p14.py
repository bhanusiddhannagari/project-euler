'''import math

for i in range (1,14):
	if i%2 == 0:
		count=0
		print (i,"i")
		#for j in range(2,i):
		while i>1:

			a=(i//2)

			#if a%2==0:
			i=a
			count+=1
			print(i,"a")	
		
			
		print(count,"count")
		if i%2!=0:
			i=3*i+1
			print(i)	
def even(d):
	d=d//2
	print(d,"d")
	return d
for i in range (1,14):
	count=0
	while i>=1:
		if i%2==0:
			print(i,"i")
			print(even(i,)) '''
max=0
a=0

c=0

for a in range (1,1000001,2):

	n=a
	
	count=1
	
	while n>=1:
			
		if n%2 == 0:
			n=n//2
			count+=1
			#print(n,"1")
		else:
			n=3*n+1
			count+=1
			#print(n,"11")
		if max<count:
				#print(b,"b")
				c=a
				max=count
		
		if n==1:
			#print(b,"b")
			#print(count,"count")

				

			break	
print(max,"count")
print(c,"c")