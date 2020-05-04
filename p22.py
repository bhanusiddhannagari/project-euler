from array import *
f=open("p22.txt","r+")
t=f.readlines()

t=str(t).replace("'","")
t=str(t).replace('"','')
t=str(t).replace('[','')
t=str(t).replace(']','')
t=(str(t).split(","))
t.sort()
b=0
#t=str(t).sort()
for i in range (0,len(t)):
	
	#print(t[i])
	a=0

	for j in range(0,len(t[i])):
		
		#print(t[i][j])
		a=a+(ord(t[i][j])-64)
	#print(a,a*(i+1),i+1,t[i])
	b=b+(a*(i+1))
print(b)

##print(t)
#for i in range(0,len(t)):
#	print(t[i],i)

