#Inclass4 Part 2

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

print "I will now count my chickens:"
# Prints that text

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4
# Prints "Hens 30" and "Roosters 97"

print "Now I will count the eggs:"
# Prints that

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# Prints 7

print "Is it true that 3 + 2 < 5 - 7?"
# Prints that text

print 3 + 2 < 5 - 7
# Prints false

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7
# Prints the text, and then the answers

print "Oh, that's why it's False."

print "How about some more."
# Prints more text

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
# Prints the text, and then the answers

#PART II

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
# Stores the strings in variables, the second has a newline for each month

print "Here are the days: ", days
print "Here are the months: ", months
# Prints the days and months

#PART III

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# Creates lists for each variable

# Prints each number in the_count
for number in the_count:
    print "This is count %d" % number

# Prints each fruit in fruits
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# 
# Use %r format when you don't know
#if the elements are strings or integers
for i in change:
    print "I got %r" % i
# Prints each element in change

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# Prints each element in elements
for i in elements:
    print "Element was: %d" % i
	
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



