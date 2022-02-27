from sys import argv
scripts, people, cats, dogs = argv
if people < cats:
    print("too many cats")
if people > cats:
    print("not many cats")
if people > dogs:
    print("world is dry")
if people < dogs:
    print("so many dogs")
