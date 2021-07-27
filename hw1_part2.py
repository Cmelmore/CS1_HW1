""" Author: Christina Elmore
    Purpose: Create a simple game of Madlibs given user inputs.
"""

print "Let's play MadLibs, CS 1."
print "Type one word responses to the following:"
print""

Name = raw_input ("proper_name ==>")
print Name
Adj = raw_input ("adjective ==>")
print Adj
Noun1 = raw_input ("noun ==> ")
print Noun1
Noun2 = raw_input ("noun ==> ")
print Noun2
Noun3 = raw_input ("noun ==> ")
print Noun3
Emote1 = raw_input ("emotion ==> ")
print Emote1
Emote2 = raw_input ("emotion ==> ")
print Emote2
Verb = raw_input ("verb ==> ")
print Verb
Noun4 = raw_input ("noun ==> ")
print Noun4

print ""
print "Here is your Mad Lib..."
print""
print "Good morning %s,"%(Name)
print "  Welcome to what promises to be a/an %s %s."%(Adj,Noun1)
print "  If you submit your %s on-time you will not lose %s\n  and you will be %s."%(Noun2,Noun3,Emote1)
print "  If you don't you will be %s and %s a poor %s."%(Emote2,Verb,Noun4)