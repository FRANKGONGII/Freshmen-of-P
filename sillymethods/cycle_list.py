the_count = [1, 2, 3, 4]
fruits = ['apple', 'orange', 'pear', 'apricot']
change = [1, 'pennies', 2, 'dimes', 3, 'quarter']
for number in the_count:
    print("this is count %d" % number)
for fruit in fruits:
    print("A fruit of type %s:" % fruit)
for i in change:
    print("I got %r" % i)

element = []
for i in range(0, 6):
    print("Adding %d to the list" % i)
    element.append(i)
for i in element:
    print("element is %d" % i)

element2 = range(0, 6)
# very interesting, we can write as print(element) -> directly print 'range(0, 6)'
for i in element2:
    print("element2 is %d" % i)
del element[1]
for i in element:
    print("element is %d" % i)


