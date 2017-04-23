#Cathrine Machingauta
#Python Lesson 2
#Playtime movies exercise
#Difficulty level: Advanced
#Last edited: 4/19/2017

#Goal #1: Create a program that will print out a list of movie titles and a set of ratings defined below into a particular format.

# First, choose any five movies you want.

# Next, look each movie up manually to find out four pieces of information:
#		Their parental guidance rating (G, PG, PG-13, R)
#		Their Bechdel Test Rating (See http://shannonvturner.com/bechdel or http://bechdeltest.com/)
#		Their IMDB Rating from 0 - 10 (See http://imdb.com/)
# 		Their genre according to IMDB

# After a few more lessons, you'll be able to tell Python to go out and get that information for you, but for now you'll have to collect it on your own.

# Now that you've written down each piece of information for all five of your movies, save them into variables.

# You'll need a variable for movie_titles, a variable for parental_rating, a variable for bechdel_rating, a variable for imdb_rating, and a variable for genre.

# Since you have five sets of facts about five movies, you'll want to use lists to hold these pieces of information.

# Once all of your information is stored in lists, loop through those lists to print out information with each part separated by a comma, like this:

# Example:
# Jurassic Park, PG-13, 3, 8.0, Adventure / Sci-Fi
# Back to the Future, PG, 1, 8.5, Adventure / Comedy / Sci-Fi

# Note how each piece of information is separated by a comma.  This is a specific file format called the "Comma Separated Value (CSV)" format
# If you can make a CSV file, you can open it up in Excel or Numbers as a spreadsheet.

# When you've printed out your information like the example above, copy/paste that into a file and save it as a .csv file.
# Open that up in Excel, Numbers, or another spreadsheet program.  How does it look?
# To see an example of how it should look, check out: https://github.com/shannonturner/python-lessons/blob/master/section_05_(loops)/movies.csv

#Attempt:

# Creating variables
Header = ['Title', 'Rating', 'Bechdel', 'IMDB', 'Genre']
Title = ['A Fish Called Wanda',"Daddy's Home",'Guardians of the Galaxy', 'Jack Reacher','S1m0ne','Hidden Figures']
Rating = ['R','PG-13','PG-13','PG-13','PG-13','PG']
Bechdel = [3,1,3,1,3,3]
IMDB = [7.6,6.1,9.0,7.0,6.1,7.9]
Genre = ['Comedy/Crime','Comedy/Family','Action/Adventure','Action/Crime','Comedy/Drama','Biography/Drama/History']
Heading = ','.join(Header)

#1. Printing to console then copying, pasting and saving file as movies.csv

##print Heading
##
##for i in range(len(Title)):
##     print str(Title[i])+",", str(Rating[i])+",", str(Bechdel[i])+",", str(IMDB[i])+",", str(Genre[i]) 


#2. Printing directly to csv:
file  = open("C:\Users\Paida\Desktop\PythonLessons\moviedata.csv",'w')
print >>file,Heading
for i in range(len(Title)):
     print >>file,str(Title[i])+",", str(Rating[i])+",", str(Bechdel[i])+",", str(IMDB[i])+",", str(Genre[i])

file.close()
