from sys import argv
script, first, second, third = argv
print("The script is called :", script)
print("Your first variable is :", first)
print("Your second variable is :", second)
print("Your third variable is :", third)

# in the upper codes, argv is the so-called argument variable, it contains arguments that we give to py
# code: script, first, second, third = argv -- mains unpack argv, and give the arguments names as script, first ...
# we call things like sys as modules or libraries
# we need to run this file in cmd ( python argument.py 1 2 3)
