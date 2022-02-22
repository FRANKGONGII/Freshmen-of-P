from sys import argv
script, user_name = argv
prompt = '>'
print("Hi %s, I'm the %s scripts. " % (user_name, script))
print("I'd like to ask you some question.")
print("Do you like me %s?" % user_name)
likes = input(prompt)
print("Where you live %s?" % user_name)
lives = input(prompt)



