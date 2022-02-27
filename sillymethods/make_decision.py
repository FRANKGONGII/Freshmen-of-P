print("you enter a dark room with two doors, do you go through door #1 or door #2?")
door = int(input('>'))
if door == 1:
    print("There is a giant bear here eating a cheese cake.What do you do?")
    print("1. take the cake")
    print("2. scream the bear")
    bear = input('>')
    if bear == '1':
        print("bear eats you!")
    elif bear == '2':
        print("bear eats you!")
    else:
        print("doing %s might better " % bear)
if door == 2:
    print("right choice!")
