from sys import argv
script, filename = argv
txt = open(filename)
print("Here is your file %r :" % filename)
print(txt.read())
print("Type filename again:")
file_again = input(">")
txt_again = open(file_again)
print(txt_again.read())

# file itself can receive some order, use filename.order_name to do that
