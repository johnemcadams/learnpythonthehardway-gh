# start with megabits
print "How many megabits per second are there?",
megabits = float(raw_input())

megabytes = float(megabits / 8)

gigabits = float(megabits / 1000)

gigabytes = float(megabits / 8000)

print """
%f megabits is equal to:
\t* megabytes %f
\t* gigabits %f
\t* gagabytes %f
""" % (megabits,megabytes,gigabits,gigabytes)