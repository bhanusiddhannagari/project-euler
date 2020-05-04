a=2
c=0
for i in range (1,1000):
	a=2*a
print(a)
b=str(a)
print(b[4])
print(len(b))
for j in range (0,len(b)):
	c=c+int(b[j])
print(c)
