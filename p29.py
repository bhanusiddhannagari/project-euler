a=[];
b=0
for i in range (2,101):
	for j in range(2,101):
		b=i**j
		if b in a:
			pass
		else:
			a.append(b)
print(len(a))