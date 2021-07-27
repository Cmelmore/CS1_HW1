""" Author: Christina Elmore
    Purpose: Create a frame composed of a given character with the given dimentions, that shows the dimentions in the lower right corner.
"""

def frame(Width,Height,Character):
    print Character * Width
    print ("%s%s%s"%(Character, " " * (Width-2), Character) + ("\n"))*(Height - 4) + ("%s%s%s"%(Character, " " * (Width-2), Character))
    print "%s%s%dx%d %s"%(Character," "*(Width - (len("%dx%d"%(Width,Height))+3)), Width, Height, Character)
    print Character * Width

Width = int(raw_input("Width of box ==> "))
print Width
Height = int(raw_input("Height of box ==> "))
print Height
Character = raw_input("Enter frame character ==> ")
print Character
print ""
print "Box"
frame(Width,Height,Character)