""" Author: Christina Elmore
    Purpose: This program reads time in minutes and seconds and distance in miles and outputs pace and speed.
"""

Minutes = int (raw_input('Minutes ==> '))
print Minutes
Seconds = int (raw_input('Seconds ==> '))
print Seconds
Miles = float (raw_input('Miles ==> '))
print Miles

SecMile = (Minutes*60 + Seconds) / Miles
PaceMin = int(SecMile/60)
PaceSec = SecMile - PaceMin*60
TimeSeconds = float((Minutes*60+Seconds))
TimeHrs = TimeSeconds/3600
Speed = Miles/TimeHrs

print ""
print "Pace is %.0f:%04.1f" %(PaceMin, PaceSec)
print "Speed is %.2f miles per hour" %(Speed)