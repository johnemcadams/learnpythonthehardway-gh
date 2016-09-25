# start with megabits
print "How many megabytes per second are there?",

megabytes = float(raw_input("megabytes: "))

megabits = float(megabytes * 8)

gigabits = float(megabytes * .008)

gigabytes = float(megabytes * .001)

print """
%f megabytes is equal to:
\t* megabits %f
\t* gigabits %f
\t* gigabytes %f
""" % (megabytes,megabits,gigabits,gigabytes)