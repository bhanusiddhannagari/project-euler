f=[]
g=[]
a=0
d=0
h=1
k=1
for i in range(10,100):
	for j in range(10,100):
		if i<j:
			
			a=i/j
			#print(a,"a",i,j)
			b=str(i)
			c=str(j)
			if b[1]==c[1] and int(b[0]) != 0 and  int(c[0]) !=0 and  int(b[1]) != 0 and  int(c[1]) !=0  :
				d=int(b[0])/int(c[0])
				#print(b[0],c[0],i,j,"1",d,"d")
				if a<1:
					if a==d :
						f.append(j)
						g.append(i)
				#print(d,"d")
				pass
			if b[0]==c[0] and  int(b[1]) != 0 and  int(c[1]) !=0  and int(b[0]) != 0 and  int(c[0]) !=0 :
				#print(b[1],c[1],i,j,"2")
				d=int(b[1])/int(c[1])
				if a<1:
					if a==d  :
						f.append(j)
						g.append(i)
				pass
			if b[0]==c[1] and int(b[0]) != 0 and  int(c[0]) !=0 and  int(b[1]) != 0 and  int(c[1]) !=0  :
				d=int(b[1])/int(c[0])
				#print(b[1],c[0],i,j,"3")
				if a<1:
					if a==d  :
						f.append(j)
						g.append(i)
				pass
			if b[1]==c[0] and int(b[0]) != 0 and  int(c[0]) !=0 and  int(b[1]) != 0 and  int(c[1]) !=0  :
				d=int(b[0])/int(c[1])
				#print(b[0],c[1],i,j,"4")
				
				if a<1:
					if a==d  :
						f.append(j)
						g.append(i)

for i in range(len(g)):
	h*=g[i]

for i in range(len(f)):
	k*=f[i]
print(k/h)
print(f,"f",g)