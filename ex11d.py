# start with megabits
print "How many gigabytes per second are there?",
gigabytes = float(raw_input())

megabits = float(gigabytes * 8000)

gigabits = float(gigabytes * 8)

megabytes = float(gigabytes * 1000)

print """
%f gigabytes is equal to:
\t* megabits %f
\t* gigabits %f
\t* megabytes %f
""" % (gigabytes,megabits,gigabits,megabytes)