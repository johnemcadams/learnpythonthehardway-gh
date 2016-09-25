# Set x as the "setup" variable using a format string
x = "There are %d types of people." % 10
# Set the binary string variable
binary = "binary"
# Set the do_not string variable
do_not = "don't"
# Set y as the punch line variable using a format string to print binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)

# Print the setup
print x
# Print the punch line
print y

# Repeat using a format string to print the setup
print "I said: %r." % x
# Repeat using a format string to print the punch line
print "I also said: '%s'." % y

# Set hilarious as a boolean
hilarious = False
# Set joke_evaluation as a string
joke_evaluation = "Isn't that joke so funny?! %r"

# Cool, print joke_evaluation and hilarious with a % sing
print joke_evaluation % hilarious

# Set the fist half of a string
w = "This is the left side of..."
# Set the second half of a string
e = "a string with a right side."

# Print both w & e by adding them
print w + e