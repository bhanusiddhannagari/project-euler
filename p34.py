import math 
from time import time
start=time()
#d=0
e=0


for i in range(14,50000):
	c=0
	d=0
	#a=(math.factorial(i))
	b=str(i)
	#print(len(b))
	for j in range (len(b)):
		c=math.factorial(int(b[j]))
		d+=c
	if d== i:
		e+=i
		#print(i)
print(e)
print("time", time()-start)




