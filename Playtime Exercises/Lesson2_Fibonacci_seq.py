#Appending 8 additional numbers to the list named series
#Print the list of 10 elements
#Fibonacci sequence -> xn = xn-1 + xn-2

series = [0,1]
for i in xrange(8):    
    series.append(series[-1] + series[-2])
    if len(series)==10:
        print series
