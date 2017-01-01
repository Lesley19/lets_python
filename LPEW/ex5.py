my_name = 'Lesley Zhang'
my_age = 24 # not a lie
my_height = 168 # centimeters
my_weight = 57 # kilograms
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "She's %d centimeters tall." % my_height
print "She's %d kilograms heavy." % my_weight
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "Her teeth are usually %s depending on the coffee." % my_teeth
#This line is tricky, try to get it exactly right
print "If I add %r, %d, and %d I get %d." % (
        my_age, my_height, my_weight, my_age + my_height + my_weight)
