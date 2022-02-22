my_name = 'Zed A.Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
print("Let's talk about %s." % my_name)
print("He's inches is %d." % my_height)
print("He's got %s eyes and %s hair" % (my_eyes, my_hair))

# these are the former uses of format-string, but since py2.6, we have got a better tool

print("{0},{1},{1}".format("my", "name"))

print("name:{name}, address {url}".format(name="cainiao", url="www.runoob.com"))

# also, the following methods, but I can't understand now
# dictionary
site = {"name": "cainiao", "url": "www.runoob.com"}
print("name:{name}, address {url}".format(**site))
 
# list 
my_list = ['cainiao', 'www.runoob.com']
print("name:{0[0]}, address {0[1]}".format(my_list))  # "0" is must

# %r can print everything in string
print("my name is %r" % my_age)

# an interesting example
y = "my name is %s" % my_name
print(y)
print("I said : %r" % y)

# another interesting example
# we will get ' ' in the these ways of print
hilarious = 'No'
joke_evaluation1 = "Isn't that joke funny? %r"
joke_evaluation2 = "Isn't that joke funny? %s"
print(joke_evaluation1 % hilarious)  # use %r
print(joke_evaluation2 % hilarious)  # use %s





