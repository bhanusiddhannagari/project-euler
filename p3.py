Number =  600851475143
i=1
while(i <= Number):
    count = 0
    if(Number % i == 0):
        j = 1
        while(j <= i):
            if(i % j == 0):
                count = count + 1
            j = j + 1
            
        if (count == 2):
            print(" %d is a Prime Factor of a Given Number %d" %(i, Number))
    i = i + 1