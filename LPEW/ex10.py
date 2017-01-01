tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm spllit\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
    \t* Cat food
    \t* Fishies
    \t* Catnip\n\t* Grass
    '''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

dog = "%s %s"
dog2 = "\tWoof!"
dog3 = "\nWang!"

print dog % (dog2, dog3)

print "%r\"" % "Dalala\'"
print "%s\"" % "Dalala\'"
