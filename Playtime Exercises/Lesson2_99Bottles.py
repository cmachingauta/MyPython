# Cathrine Machingauta
# Lesson 2 - Loops and range
# Difficulty level: Beginner

# Can you make Python print out the song for 99 bottles of beer on the wall?
# Using range() and a loop, print out the song.

for number in range(99,1,-1):
    print "{0} bottles of beer on the wall, {0} bottles of beer...".format(number)
    print "If one of those bottles should happen to fall,{0} bottles of beer on the wall".format(number-1)
