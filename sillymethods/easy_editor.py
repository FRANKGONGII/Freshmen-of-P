from sys import argv
script, filename = argv
print("We're going to erase %r. " % filename)
print("If you don't want that, hit ^c")
print("If you do want that, hit return")
input("?")
print("Opening the file...")

# 'w' mains the mode (write)
target = open(filename, 'w')

print("Truncating the file. Bye!")
target.truncate()
print("Now I'm going to ask you for three lines.")
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")
print("I'm going to write these to the file")
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')
print("finish")
print("Do you want to check what you write?")
print("If you don't want that, hit ^c")
print("If you do want that, hit return")
input("?")
target = open(filename, 'r')
print(target.read())
target.close()


