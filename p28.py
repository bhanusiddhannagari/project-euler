a=1001
#a=int(input("enter no of rows"))
n=[[0 for x in range(a)]for j in range(a)]

b=a*a
c=0
d=0
f=0
count=int((a+1)/2)
low=0
high=a-1
for i in range(count):
	for j in range(low,high+1):
		n[i][j]=b
		b=b-1
	for j in range(low+1,high+1):
		n[j][high]=b
		b=b-1
	for j in range(high-1,low-1,-1):
		n[high][j]=b
		b=b-1
	for j in range(high-1,low,-1):
		n[j][low]=b
		b=b-1
	low=low+1
	high=high-1


'''for i in range(a):
	for j in range(a):
		
		print(n[i][j],end="\t")
	print()'''
for i in range(0,a):
	#print(n[i][i])
	c=c+int(n[i][i])

for i in range(a-1,-1,-1):
	d=d+int(n[f][i])
	#print(n[f][i])
	f=f+1
#print(d)
e=c+d-1
print("sum:",e)


