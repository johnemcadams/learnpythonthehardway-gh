# playing around with quotes and the back slash character

print("I am 6'4\" tall.") # escape a double-quote inside string
print('I am 6\'4" tall.') # escape single-quote inside string

# escape a tab
tabby_cat = "\tI'm tabbed in."
# escape a new line
persian_cat = "I'm split\non a line."
# escape the back slash character
backslash_cat = "I'm \\ a \\ cat."

# use triple quotes to write several lines
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# print out the variables
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat
print u'\U0001F47E'
while True:
    for i in ["/","-","|","\\","|","\v"]:
        print "%s\r" % i,
        
