import math
a=0
c=0
for i in range(1,1000000):
	a+=i
	count=0
	for j in range (1,int(math.ceil(math.sqrt(a)))):
		if a%j==0:
			#print(a,"a")
			count+=2
			if count == 500:
				c=count
				print(a)
				break
				if c==500:
					print(a,"a")
					break#
		
				


"""def divisiors(b):
	for i in range(12362,123000):
		c=0
		a=76403341
		#print(i,"i")
		a+=i
		#print(a,"a")
		count=0
		for j in range (1,int(math.ceil(math.sqrt(a)))):
			if a%j==0:
				#print(a,"a")
				count+=2
				c=count
				if c == b:
					print(a)
					print(c)
					return a
print(divisiors(500))
"""

		
		
"""if count>=500:
				c=a
				#break
				print(c)"""
				
							
		
"""import math
from time import time
b=0
t = time()
def divisors(n):
	
    number_of_factors = 0
    print(n)
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        b=n
        if n % i == 0:
            number_of_factors +=2
        else:
            continue
    return number_of_factors

x=1
for y in range(2,1000000):
    x += y
    if divisors(x) >= 500:
        print (x,("X"))
        break
tt = time()-t
print (tt)
#print(b)"""