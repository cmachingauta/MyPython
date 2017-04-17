#Cathrine Machingauta
#Python Lesson 2 - Playtime Exercise
#PB&J - Difficulty level: Beginner


#Goal #1: Write a new version of the PB&J program that uses a while loop.
##Print "Making sandwich #" and the number of the sandwich until you are
##out of bread, peanut butter, or jelly.

bread = 10
pb = 5
jelly = 5

counter=0
while ((bread>=2) and (pb>=1) and (jelly>=1)):
	print "Making sandwich #{}".format(counter+1)
	bread=bread-2
	pb=pb-1
	jelly=jelly-1
	counter+=1
print "All done; only had enough bread for {} sandwiches".format(counter)

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.
counter=0
while ((bread>=2) & (pb>=1) & (jelly>=1)):
    print "Making sandwich #{}".format(counter+1)
    if (bread-2>=2 and pb-1>=1 and jelly-1>=1):
        print "You have enough bread for {} more sandwiches," \
        "enough peanut butter for {} more," \
        "and enough jelly for {} more.".format(((bread-2)/2),(pb-1),(jelly-1))
    elif (bread-2==1 and pb-1>=1 and jelly-1>=1):
        print "You could make an additional open-faced sandwich with the remaining slice of bread"
    elif (bread-2<2 and pb-1>=1 and jelly-1>=1):
        print "All done, you ran out of bread"
    elif (bread-2>=2 and pb-1<1 and jelly-1>=1):
        print "All done, you ran out of peanut butter"
    elif (bread-2>=2 and pb-1>=1 and jelly-1<1):
        print "All done, you ran out of jelly"
    elif (bread-2<2 and pb-1<1 and jelly-1>=1):
        print "All done, you ran out of bread and peanut butter"
    elif (bread-2<2 and pb-1>=1 and jelly-1<1):
        print "All done, you ran out of bread and jelly"
    elif (bread-2>=2 and pb-1<1 and jelly-1<1):
        print "All done, you ran out of jelly and peanut butter"
    else:
        print "All done, you ran out of all ingredients"
    bread=bread-2 
    pb=pb-1 
    jelly=jelly-1 
    counter+=1
#Question: How can I do this with fewer lines of code?"
  
