# importing the calendar module
import calendar
from datetime import date
COUNT=0
for i in range (1901,2001):
	for j in range (1,13):
		if date(i,j,1).weekday()==6:
			COUNT+=1
print(COUNT)
#