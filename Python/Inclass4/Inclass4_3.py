#Inclass4 Part 3

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

#Use the code from Lecture14.py to create and change the 
#'stuff' list; Then comment on each line of the code below
#what it does, and what the result is

print stuff[1] #First element of stuff
print stuff[-1] #Last element of stuff
print stuff.pop() #Prints and removes the last element of the list
print ' '.join(stuff) #Concatenates list values with a space
print '#'.join(stuff[3:5]) #Concatenates list values 3-5 with a #

#PART II

#Create comments where marked with # to explain the code below

# A list of duples for states
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# A list of duples for cities
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Creates new list elements
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# 
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# Prints 10 '-'s and then the abbreviations for both states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# Prints 10 '-'s and then all the cities in the respective states
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# Prints each state and it's abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# Prints each state and which city it "has"
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# Prints each state, its abbreviation, and it's city
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])



