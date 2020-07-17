a=[200,100,50,20,10,5,2,1]
count=0
b=0
for p in range(0,2):
	b=b*a[0]*p
	if b==200:
		count+=1
		break
	else:
		b=a[0]*p
		for o in range(0,3):
			b=b+a[1]*o
			if b==200:
				count+=1
				break
			else:
				b=a[1]*o
			for n in range (0,5):
				b=b+a[2]*n
				if b == 200:
					count+=1
					break
				else:
					b=a[1]*o+a[2]*n
				for m in range(0,11):
					b=b+a[3]*m
					if b==200:
						count+=1
						break
					else:
						b=a[1]*o+a[2]*n+a[3]*m

					for l in range(0,21):
						b=b+a[4]*l
						if b==200:
							count+=1
							break
						else:
							b=a[4]*l+a[1]*o+a[2]*n+a[3]*m



						for k in range(0,41):
							b=b+a[5]*k
							if b==200:
								count+=1
								break
							else:
								b=a[5]*k+a[4]*l+a[1]*o+a[2]*n+a[3]*m




							for j in range(0,101):
								b=b+a[6]*j

								if b==200:
									count+=1
									break
								else:
									b=a[6]*j+a[5]*k+a[4]*l+a[1]*o+a[2]*n+a[3]*m
									#print(b)



								for i in range(0,201):
									b=b+a[7]*i
									if b >200:
										break

									if b==200:
										count+=1
										break
									else:
										b=a[6]*j+a[5]*k+a[4]*l+a[1]*o+a[2]*n+a[3]*m
				
print(count)		