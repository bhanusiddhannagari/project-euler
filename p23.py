g=0
c=0
d=[]
e=[]
h=[]
#f=open("p23.txt","w+")
for i in range (1,28123):
	h.append(i)
print(sum(h))

for i in range (12,28123):
	a=0

	#print(i)
	for j in range (1,i):
		#print(j,"j")
		if i%j == 0:
			a=a+j

	if a>i:
		#print(i)
		#c=c+i
		d.append(i)
print(d)
print(len(d))
print(len(d))
for i in range(0,len(d)):
	for j in range(i,len(d)):
		if d[i]+d[j] <28123 :
			#print(d[i]+d[j])
			h[(d[i]+d[j])-1]= 0
print(h)
print(sum(h))
