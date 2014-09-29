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