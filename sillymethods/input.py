print("How old are you?", end="")
age = int(input())
print("How tall are you?", end="")
height = int(input())
print("How much do you weight?", end="")
weight = int(input())
print("So you are %r old, %r tall, %r heavy" % (age, height, weight))
a = input("your name:")
print(a)
# if we write like the book as %r and raw_input(), we will get '', so we need to change string into int