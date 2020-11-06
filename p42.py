a=0
b=[]
for i in range (1,351):
	a=a+i
	b.append(a)
from array import *
f=open("p42.txt","r+")
t=f.readlines()
#t=str(t).replace("'","")
t=str(t).replace('"','')
# t=str(t).replace('[','')
# t=str(t).replace(']','')
t=(str(t).split(","))
t.sort()
# print(type(t))
# print(len(t))
count=0
# for i in range (0,len(t)):
# 	print(t[i],i)
for i in range (0,len(t)):
	#print(t[i])
	d=0
	for j in range(0,len(t[i])):
		
		#print(t[i][j])
		d=d+(ord(t[i][j])-64)
	#print(d,type(d))	
	if d in b:
		count+=1
print(count)


a=0
b=[]
for i in range (1,351):
	a=a+i
	b.append(a)
from array import *
f=open("p42.txt","r+")
t=f.readlines()
t=str(t).replace('"','')
t=(str(t).split(","))
t.sort()
count=0
for i in range (0,len(t)):	
	d=0
	for j in range(0,len(t[i])):	
		d=d+(ord(t[i][j])-64)
	if d in b:
		count+=1
print(count,i)







