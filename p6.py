sum1 = 0
sum2 = 0
for i in range (1,101):
	a=i*i
	sum1=sum1+a
print (sum1)
for i in range (1,101):
	sum2=sum2+i
b=sum2*sum2
print (b)
c=b-sum1
print(c)
