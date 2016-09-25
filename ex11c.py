# start with megabits
print "How many gigabits per second are there?",
gigabits = float(raw_input())

megabits = float(gigabits * 1000)

megabytes = float(gigabits * 125)

gigabytes = float(gigabits * .125)

print """
%f gigabits is equal to:
\t* megabits %f
\t* megabytes %f
\t* gigabytes %f
""" % (gigabits,megabits,megabytes,gigabytes)