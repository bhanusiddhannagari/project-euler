import inflect
import string
a=0
for i in range (1,1001):
	p=inflect.engine()
	w=p. number_to_words(i)
	w=w.replace("-","")
	w=w.replace(" ","")
	w=w.replace(",","")
	a=a+len(w)
print(a)
